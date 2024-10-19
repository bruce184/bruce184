void BFS(const dothi &G, dinh start) {
    // Khởi tạo mảng đánh dấu đã thăm
    bool* visited = new bool[30];
    for (int i = 0; i < 30; ++i){ visited[i] = false;}

    // Khởi tạo mảng động cho hàng đợi
    dinh* queue = new dinh[30]; // static size: 30
    int front = 0;
    int rear = 0;

    // Đánh dấu đỉnh bắt đầu là đã thăm và thêm vào hàng đợi
    visited[start] = true;
    queue[rear++] = start;

    // Xử lý hàng đợi
    while (front < rear) {
        dinh u = queue[front++]; // Lấy đỉnh từ đầu hàng đợi
        cout << u << " "; // In đỉnh
        // Lấy các đỉnh kề
        dinh adjacentVertices[30];
        int count = getAdjacentVertices(G, u, adjacentVertices);
        for (int i = 0; i < count; ++i) {
            dinh v = adjacentVertices[i];
            if (!visited[v]) { // Nếu đỉnh v chưa được thăm
                visited[v] = true; // Đánh dấu đỉnh v đã thăm
                queue[rear++] = v; // Thêm đỉnh v vào hàng đợi
            }
        }
    }

    // Giải phóng bộ nhớ
    delete[] visited;
    delete[] queue;
}
