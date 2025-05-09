# from fastapi import FastAPI

# app = FastAPI()
# app.get("/")
# def index():
#     return {"message": "Hello World"}
    
# app.get("/hello")
# def hello():
#     return {"message": "Hello from FastAPI"}
def la_so_nguyen_to(n):
    if n < 2:
        return False  # Các số nhỏ hơn 2 không phải là số nguyên tố

    # Duyệt từ 2 đến căn bậc hai của n
    can_bac_hai = int(n ** 0.5) + 1  # Lấy phần nguyên của căn bậc hai rồi cộng thêm 1
    for i in range(2, can_bac_hai):
        if n % i == 0:
            # Nếu n chia hết cho một số trong khoảng này thì không phải số nguyên tố
            return False
    return True  # Nếu không chia hết cho số nào thì là số nguyên tố

# In ra các số nguyên tố từ 2 đến 30
for num in range(2, 31):
    if la_so_nguyen_to(num):
        print(f"{num} là số nguyên tố")