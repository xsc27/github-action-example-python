# Hello World Example 3

<!-- action-docs-description -->

## Description

A Hello World GitHub Action example with Python with a proper CLI.

<!-- action-docs-description -->

### Why

- Lets use `argparse` for our CLI. This will be helpful when we have more parameters.

### How

- Add `action.py` shim as the entrypoint for the container.

<!-- action-docs-inputs -->

## Inputs

| parameter | description   | required | default |
| --------- | ------------- | -------- | ------- |
| name      | Who to greet. | `false`  | World   |

<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

## Outputs

| parameter | description |
| --------- | ----------- |
| greeting  | Greeting    |

<!-- action-docs-outputs -->
