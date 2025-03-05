from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Cho phép CORS để frontend gọi API từ trình duyệt
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lưu trạng thái lưới (giả lập database)
grid_state = {}
grid_size = 10  # Kích thước ban đầu

# Model nhận dữ liệu từ frontend
class CellUpdate(BaseModel):
    x: int
    y: int
    color: str

@app.post("/update-cell")
async def update_cell(data: CellUpdate):
    key = f"{data.x},{data.y}"

    if data.color == "white":
        grid_state.pop(key, None)  # Nếu xóa màu, chỉ xóa khỏi grid_state
    else:
        grid_state[key] = data.color  # Nếu tô màu, cập nhật màu mới

    # Nếu ô ngoài cùng và không ở chế độ xóa, mở rộng lưới
    global grid_size
    if data.color != "white" and (data.x == 0 or data.x == grid_size - 1 or data.y == 0 or data.y == grid_size - 1):
        grid_size += 1

    return {"status": "success", "grid": grid_state, "grid_size": grid_size}

@app.post("/restart-grid")
async def restart_grid():
    global grid_state, grid_size
    grid_state = {}
    grid_size = 10
    return {"status": "success"}

@app.get("/get-grid")
async def get_grid():
    return {"grid": grid_state, "grid_size": grid_size}
