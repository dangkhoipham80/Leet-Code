const gridContainer = document.getElementById("grid-container");
const grid = document.getElementById("grid");
const colorPicker = document.getElementById("colorPicker");
const modeToggle = document.getElementById("modeToggle");
const restartButton = document.getElementById("restartButton");

const API_URL = "http://127.0.0.1:8000"; // Backend FastAPI

let gridSize = 10; // Kích thước ban đầu
let isEraseMode = false; // Chế độ: false = Tô màu, true = Xóa màu

// Cập nhật trạng thái nút chế độ
modeToggle.addEventListener("click", () => {
    isEraseMode = !isEraseMode;
    modeToggle.textContent = isEraseMode ? "Chế độ: Xóa màu" : "Chế độ: Tô màu";
});

// Tạo lưới ban đầu
function createGrid(gridData) {
    grid.innerHTML = "";
    grid.style.gridTemplateColumns = `repeat(${gridSize}, 40px)`;

    for (let row = 0; row < gridSize; row++) {
        for (let col = 0; col < gridSize; col++) {
            const cell = document.createElement("div");
            cell.classList.add("cell");
            cell.dataset.x = row;
            cell.dataset.y = col;

            if (gridData && gridData[`${row},${col}`]) {
                cell.style.backgroundColor = gridData[`${row},${col}`];
            } else {
                cell.style.backgroundColor = "white";
            }

            cell.addEventListener("click", () => handleCellClick(row, col, cell));
            grid.appendChild(cell);
        }
    }
}

// Xử lý khi click vào ô
function handleCellClick(row, col, cell) {
    const color = isEraseMode ? "white" : colorPicker.value; // Chế độ xóa thì màu trắng

    fetch(`${API_URL}/update-cell`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ x: row, y: col, color })
    })
    .then(response => response.json())
    .then(data => {
        if (data.grid[`${row},${col}`]) {
            cell.style.backgroundColor = color; // Tô màu
        } else {
            cell.style.backgroundColor = "white"; // Xóa màu
        }

        // ✅ Chỉ mở rộng lưới nếu đang ở chế độ tô màu
        if (!isEraseMode && data.grid_size > gridSize) {
            gridSize = data.grid_size;
            createGrid(data.grid);
        }
    });
}

// Nút "Restart" để xóa toàn bộ lưới
restartButton.addEventListener("click", () => {
    fetch(`${API_URL}/restart-grid`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(() => {
        gridSize = 10; // Đặt lại kích thước lưới ban đầu
        createGrid({});
    });
});

// Lấy trạng thái lưới khi tải lại trang
fetch(`${API_URL}/get-grid`)
    .then(response => response.json())
    .then(data => {
        gridSize = data.grid_size;
        createGrid(data.grid);
    });
