# HTTP Status Cat Example

<!-- action-docs-description -->

## Description

A GitHub action example using HTTP Status Cats with Pydantic!

<!-- action-docs-description -->

### Note

- We now have dependencies, so we will make this a proper Python package with `pyproject.toml`.
- We now require multiple parameters, which is getting complicated.

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
