# Usage

```bash
cd frontend
quasar build
cd ..
rm -rf backend/static
mv frontend/dist/spa backend/static
cd backend
uvicorn --reload main:app
```