import yaml
from jinja2 import Environment, FileSystemLoader
import os

# Configuration
YAML_FILE = 'navigation.yml'
TEMPLATE_FILE = 'template.html'
OUTPUT_DIR = '.'  # Output to the current directory

# Global configuration keys (the script will skip these when looking for pages)
RESERVED_KEYS = ['page_title', 'column_title', 'left_column', 'google', 'zjuers', 'logo', 'banner']

# Column splitting logic configuration
LINE_LIMIT_PER_COLUMN = 23  # Maximum number of lines per column
HEADER_WEIGHT = 3           # A main header (H2) counts as 3 lines

def split_content_into_columns(content_data):
    """
    Splits page content into two columns based on a line-count weight.
    
    Args:
        content_data (list): The list of page content from the YAML file.
        
    Returns:
        tuple: A tuple containing the content for the two columns (column1_data, column2_data).
    """
    column1 = []
    column2 = []
    current_line_count = 0
    
    # Flag to indicate when the first column is full; all subsequent content goes to the second column.
    is_col1_full = False

    for category_item in content_data:
        # Get the category title and the list of links.
        # .items() returns a view, so we convert it to a list to get the first element.
        category_title, links = list(category_item.items())[0]
        
        # Calculate the total line height of the current card.
        # Each link counts as 1 line, plus the weight of the header.
        card_line_height = HEADER_WEIGHT + len(links)

        if is_col1_full:
            # If the first column is already full, add the card directly to the second column.
            column2.append(category_item)
            continue

        # Check if adding this card would exceed the limit for the first column.
        if (current_line_count + card_line_height) > LINE_LIMIT_PER_COLUMN and current_line_count > 0:
            # If it would exceed the limit, and the first column is not empty,
            # set the flag and put this card into the second column.
            is_col1_full = True
            column2.append(category_item)
        else:
            # Otherwise, add the card to the first column and increment the line count.
            column1.append(category_item)
            current_line_count += card_line_height
            
    return column1, column2


def main():
    """Main function to build the static site."""
    print("Starting to build the static site (with auto-columns) ...")

    # 1. Read the YAML file
    try:
        with open(YAML_FILE, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            print(f"Successfully read data source: {YAML_FILE}")
    except FileNotFoundError:
        print(f"Error: Could not find the file {YAML_FILE}!")
        return
    
    # 2. Set up the Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(TEMPLATE_FILE)
    print(f"Successfully loaded template: {TEMPLATE_FILE}")

    # 3. Automatically discover and iterate through pages
    for page_name, page_content in data.items():
        if page_name in RESERVED_KEYS:
            continue

        output_filename = f"{page_name}.html"
        print(f"Processing page: {output_filename}...")
        
        # 4. Call the split function to divide content into columns
        content_col1, content_col2 = split_content_into_columns(page_content)
        print(f" Content split into two columns.")
        
        # 5. Render the template
        html_content = template.render(
            **data,
            current_page=output_filename,
            content_col1=content_col1,  # Pass the data for the first column
            content_col2=content_col2   # Pass the data for the second column
        )

        # 6. Write the content to an HTML file
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Successfully saved to {output_path}.")

    print("Website build complete!")


if __name__ == '__main__':
    main()