from fastapi import FastAPI

app = FastAPI(
    title="Auth Service",
    description="Handles authentication, authorization, roles, and licensing.",
    version="0.1.0"
)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

# Placeholder for future routers
# from .api import users_router, roles_router, subscription_router
# app.include_router(users_router, prefix="/users", tags=["Users"])
# app.include_router(roles_router, prefix="/roles", tags=["Roles"])
# app.include_router(subscription_router, prefix="/subscription", tags=["Subscription"])
