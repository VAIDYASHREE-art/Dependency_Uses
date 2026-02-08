from fastapi import FastAPI
from starlette.middleware.gzip import GZIPMiddleware

app = FastAPI()

app.add_middleware(
    GZIPMiddleware,
    minimum_size=1000  # Compress responses larger than 1000 bytes
)

# The middleware compresses responses larger than the specified minimum size using GZIP compression.