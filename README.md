# jesa-ui

## Prerequisites

This package requires [Tailwind CSS](https://tailwindcss.com/) to be installed in your project (globally or locally) before use.

Install Tailwind CSS using npm:

```sh
npm install -D tailwindcss
```

## Installation

Install this package using pip:

```sh
pip install jesa-ui
```

## Usage

After installing Tailwind CSS and this package, you can use the CLI to install UI components:

```sh
jesa-ui install button --to <your-components-dir>
```

This will copy the specified component (e.g., `button`) into your project's components directory.

### Example Usage

Here's how to use the button component in your templates:

```html
<div class="flex flex-col justify-center items-center space-y-4">
  {% import "components/button.j2" as Component %} {{
  Component.Button(type="button", label="Default Button", class_="w-full",
  disabled=false) }} {{ Component.Button(type="button", label="Disabled Button",
  class_="w-full", disabled=true) }}
</div>
```

## Notes

- This package is framework-agnostic and can be used with any Python web framework (e.g., Flask, Django, FastAPI, etc.).
- Make sure you have Tailwind CSS set up in your project to process the provided component templates.

## License

MIT
