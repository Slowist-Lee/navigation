# Customizable Static Navigation Page

>[!NOTE]
> Mostly Written by AI
>

**[Demo](https://navigation.slowist.top/)**

A simple, fast, and highly customizable static navigation page. managed through a single YAML configuration file (`navigation.yml`).

The final HTML is automatically generated and deployed using a Python script and GitHub Actions.


## How to Customize Your Page

Modifying the content of your navigation page is incredibly simple.

1.  **Open the `navigation.yml` file.**
2.  **Edit the content** following the structure below.
3.  **Commit and push** your changes to the `master` branch.

That's it! The GitHub Actions workflow will automatically update your live site in a minute or two.

### `navigation.yml` Structure

Here is a basic overview of the configuration file:

```yaml
# Sets the title of the browser tab
page_title: "My Awesome Navigation Page"

# Defines the links in the left-hand sidebar menu
left_column:
  - name: Home
    url: index.html
  - name: Another Page
    url: another.html # You can create more pages

# Defines the content for the 'index.html' page
index:
  # Each item in the list becomes a card with a title.
  # The key ("My Favorite Tools") becomes the card's H2 title.
  - My Favorite Tools:
      # The list of key-value pairs becomes the links.
    - Link Name 1: https://example.com/
    - Link Name 2: https://example.org/
  
  - Another Category:
    - Another Link: https://example.net/
```

## Features

-   **YAML-Driven Content**: No need to edit HTML directly. Manage all your links, titles, and categories in `navigation.yml`.
-   **Static Site Generation**: A simple Python script (`build.py`) using Jinja2 renders the static HTML files.
-   **Automatic Deployment**: Push changes to the `master` branch, and GitHub Actions automatically builds and deploys the site to GitHub Pages.
-   **Smart Multi-Column Layout**: The build script automatically splits content into two columns to ensure a balanced and readable layout.

## More Customization

- modifying `template.html` and `main.css` for more customization.