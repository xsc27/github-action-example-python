# Hello World Example 3

<!-- action-docs-description -->

## Description

A Hello World GitHub Action example with Python with outputs.

<!-- action-docs-description -->

### Why

- We can pass data to other parts of our CI pipeline.

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
