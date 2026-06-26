# Backend Tests

This repository includes FastAPI backend tests under the `tests/` directory.

## Run tests

From the repository root, run:

```bash
pytest tests
```

## Test framework

- `pytest` is used for running tests
- `fastapi.testclient.TestClient` is used to exercise the FastAPI application
- `tests/conftest.py` resets the in-memory activity data between tests
