class Player:
    def __init__(self, player_id, name, speed_score, technique_score, goal_score):
        self.id = player_id
        self.name = name
        self.speed_score = speed_score
        self.technique_score = technique_score
        self.goal_score = goal_score
        self.average_score = 0
        self.performance_type = ""
        self.calculate_average()
        self.classify_performance()

    def calculate_average(self):
        self.average_score = round(
            self.speed_score * 0.3 + self.technique_score * 0.4 + self.goal_score * 0.3, 2
        )

    def classify_performance(self):
        if self.average_score < 5.0:
            self.performance_type = "Dự bị yếu"
        elif self.average_score < 6.5:
            self.performance_type = "Trung bình"
        elif self.average_score < 8.0:
            self.performance_type = "Tốt"
        else:
            self.performance_type = "Ngôi sao"

    def __str__(self):
        return f"{self.id:<10}{self.name:<20}{self.speed_score:<10}{self.technique_score:<10}{self.goal_score:<10}{self.average_score:<15}{self.performance_type}"

class PlayerManager:
    def __init__(self):
        self.players = []

    def add_player(self):
        player_id = input("Nhập mã cầu thủ: ").strip()
        if not player_id:
            print("Mã cầu thủ không được rỗng")
            return
        if any(p.id == player_id for p in self.players):
            print("Mã cầu thủ đã tồn tại")
            return

        name = input("Nhập họ tên cầu thủ: ").strip()
        if not name:
            print("Họ tên không được rỗng")
            return

        try:
            speed = float(input("Nhập điểm tốc độ : "))
            technique = float(input("Nhập điểm kỹ thuật : "))
            goal = float(input("Nhập điểm ghi bàn : "))
        except ValueError:
            print("Điểm phải là số ")
            return
        if not all(0 <= x <= 10 for x in [speed, technique, goal]):
            print("Điểm phải nằm trong khoảng 0-10 ")
            return

        player = Player(player_id, name, speed, technique, goal)
        self.players.append(player)
        print("Thêm cầu thủ thành công")

    def show_all(self):
        if not self.players:
            print("Danh sách cầu thủ đang rỗng")
            return
        print(f"{'Mã':<10}{'Họ tên':<20}{'Tốc độ':<10}{'Kỹ thuật':<10}{'Ghi bàn':<10}{'Phong độ':<15}{'Phân loại'}")
        for p in self.players:
            print(p)

    def update_player(self):
        player_id = input("Nhập mã cầu thủ cần cập nhật: ").strip()
        player = next((p for p in self.players if p.id == player_id), None)
        if not player:
            print("Không tìm thấy cầu thủ cần cập nhật ")
            return

        try:
            player.speed_score = float(input("Nhập điểm tốc độ mới : "))
            player.technique_score = float(input("Nhập điểm kỹ thuật mới : "))
            player.goal_score = float(input("Nhập điểm ghi bàn mới : "))
        except ValueError:
            print("Điểm phải là số")
            return

        if not all(0 <= x <= 10 for x in [player.speed_score, player.technique_score, player.goal_score]):
            print("Điểm phải nằm trong khoảng 0-10")
            return

        player.calculate_average()
        player.classify_performance()
        print("Cập nhật cầu thủ thành công ")

    def delete_player(self):
        player_id = input("Nhập mã cầu thủ cần xóa: ").strip()
        player = next((p for p in self.players if p.id == player_id), None)
        if not player:
            print("Không tìm thấy cầu thủ cần xóa ")
            return

        confirm = input("Bạn có chắc muốn xóa cầu thủ này không? (Y/N): ").strip().lower()
        if confirm == "y":
            self.players.remove(player)
            print("Xóa cầu thủ thành công ")
        elif confirm == "n":
            print("Đã hủy thao tác ")
        else:
            print("Nhập chưa đúng ")

    def search_player(self):
        keyword = input("Nhập tên cầu thủ cần tìm: ").strip().lower()
        results = [p for p in self.players if keyword in p.name.lower()]
        if not results:
            print("Không tìm thấy cầu thủ phù hợp!")
            return
        print(f"{'Mã':<10}{'Họ tên':<20}{'Tốc độ':<10}{'Kỹ thuật':<10}{'Ghi bàn':<10}{'Phong độ':<15}{'Phân loại'}")
        for p in results:
            print(p)


def show_menu():
    print("""
1. Hiển thị danh sách cầu thủ
2. Thêm cầu thủ mới
3. Cập nhật thông tin cầu thủ
4. Xóa cầu thủ
5. Tìm kiếm cầu thủ
6. Thoát
""")


def main():
    manager = PlayerManager()
    while True:
        show_menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()
        if choice == "1":
            manager.show_all()
        elif choice == "2":
            manager.add_player()
        elif choice == "3":
            manager.update_player()
        elif choice == "4":
            manager.delete_player()
        elif choice == "5":
            manager.search_player()
        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý cầu thủ bóng đá ")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")


if __name__ == "__main__":
    main()

        