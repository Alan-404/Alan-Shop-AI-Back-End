from fastapi import FastAPI
from password_check.password_service_check import PasswordCheckService
from pydantic import BaseModel
app = FastAPI()


# Check Strength Password API
password_check_service = PasswordCheckService()

class InputPasswordCheck(BaseModel):
    password: str

@app.post('/password/check')
def check_strength(data: InputPasswordCheck):
    return int(password_check_service.predict(data.password))