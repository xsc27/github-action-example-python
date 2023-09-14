# HTTP Status Cat Example 4

<!-- action-docs-description -->

## Description

A GitHub action example using HTTP Status Cats with Pydantic and Typer!

<!-- action-docs-description -->

### Note

- Typer makes our CLI cleaner.
- Thank you to Sebastián Ramírez Montaño, for the inspiration, and Typer

<!-- action-docs-inputs -->

## Inputs

| parameter | description      | required | default |
| --------- | ---------------- | -------- | ------- |
| http_code | HTTP Status Code | `true`   |         |
| api_token | API Token        | `true`   |         |

<!-- action-docs-inputs -->

<!-- action-docs-outputs -->

## Outputs

| parameter | description            |
| --------- | ---------------------- |
| title     | HTTP status code title |
| image     | Image URL              |
| data      | JSON response          |

<!-- action-docs-outputs -->
