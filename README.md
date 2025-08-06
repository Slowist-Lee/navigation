# Customizable Static Navigation Page

**[Demo](https://navigation.slowist.top/)**

A simple, fast, and highly customizable static navigation page. managed through a single YAML configuration file (`navigation.yml`).

The final HTML is automatically generated and deployed using a Python script and GitHub Actions.

### Configuration Structure

The configuration is written in `navigation.yml`. Here is a basic overview of the configuration file:

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

## More Customization

- modifying `template.html` and `main.css` for more customization.