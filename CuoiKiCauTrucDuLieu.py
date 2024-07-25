from datetime import datetime

class Person:
    def __init__(self, name, gender, birth_place, date_of_birth, date_of_death, job):
        self.name = name
        self.gender = gender
        self.birth_place = birth_place
        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_death
        self.job = job
        self.left = None  # Con bên trái
        self.right = None  # Con bên phải

class FamilyTree:
    def __init__(self):
        self.root = None

    def add_person(self, person, parent_name=None):
        if self.root is None:
            self.root = person
        else:
            self._add_person(self.root, person, parent_name)

    def _add_person(self, node, person, parent_name):
        if node is None:
            return False
        if node.name == parent_name:
            if not node.left:
                node.left = person
            elif not node.right:
                node.right = person
            else:
                print("Đã có đủ 2 con.")
            return True
        else:
            added = self._add_person(node.left, person, parent_name)
            if not added:
                added = self._add_person(node.right, person, parent_name)
            return added

#Cau 2
    def print_family_tree(self, node=None, generation=1):
        if node is None:
            node = self.root
        if node is not None:
            status = "Còn sống" if not node.date_of_death else "Đã mất"
            print(f"Đời {generation}: Tên: {node.name}, Giới tính: {node.gender}, Nơi sinh: {node.birth_place}, Ngày sinh: {node.date_of_birth}, Nghề nghiệp: {node.job}, Trạng thái: {status}")
            if node.left:
                self.print_family_tree(node.left, generation + 1)
            if node.right:
                self.print_family_tree(node.right, generation + 1)
                
#Cau 3                
    def find_person(self, name):
        generation = 1  # Đời thứ nhất là người sáng lập gia phả
        person, generation = self._find_person(self.root, name, generation)
        if person:
            print(f"Thông tin thành viên: {person.name}, {person.gender}, {person.birth_place}, {person.date_of_birth}, {person.job}")
            print(f"Đời thứ: {generation}")
        else:
            print("Không tìm thấy")

    def _find_person(self, node, name, generation):
        if node is None:
            return None, generation
        if node.name == name:
            return node, generation
        left_search, gen_left = self._find_person(node.left, name, generation + 1)
        if left_search:
            return left_search, gen_left
        return self._find_person(node.right, name, generation + 1)

#Cau 4
    def calculate_total_age_of_living_members(self, node=None):
        if node is None:
            node = self.root
        total_age = 0
        if node is not None:
            if not node.date_of_death:  # Kiểm tra nếu thành viên vẫn còn sống
                birth_date = datetime.strptime(node.date_of_birth, "%d-%m-%Y")
                age = (datetime.now() - birth_date).days // 365
                total_age += age
            if node.left:
                total_age += self.calculate_total_age_of_living_members(node.left)
            if node.right:
                total_age += self.calculate_total_age_of_living_members(node.right)
        return total_age

#Cau 5
    def print_members_without_children(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            # Kiểm tra nếu thành viên không có con
            if node.left is None and node.right is None:
                print(f"Thành viên không có con: {node.name}")
            # Duyệt qua cây con bên trái và bên phải
            if node.left:
                self.print_members_without_children(node.left)
            if node.right:
                self.print_members_without_children(node.right)

#Cau 6
    def print_members_of_generation(self, generation_to_print, node=None, current_generation=1):
        if node is None:
            node = self.root
        if node is not None:
            if current_generation == generation_to_print:
                print(f"Đời {current_generation}: {node.name}")
            if node.left:
                self.print_members_of_generation(generation_to_print, node.left, current_generation + 1)
            if node.right:
                self.print_members_of_generation(generation_to_print, node.right, current_generation + 1)
                
#Cau 7
    def get_living_members(self, node=None):
        if node is None:
            node = self.root
        living_members = []
        if node is not None:
            if not node.date_of_death:  # Kiểm tra nếu thành viên vẫn còn sống
                living_members.append(node)
            if node.left:
                living_members.extend(self.get_living_members(node.left))
            if node.right:
                living_members.extend(self.get_living_members(node.right))
        return living_members
        
    def print_living_members_sorted_by_age(self):
        living_members = self.get_living_members()
        # Sắp xếp theo tuổi từ lớn đến nhỏ
        living_members.sort(key=lambda member: (
            datetime.now().year - datetime.strptime(member.date_of_birth, "%d-%m-%Y").year,
            datetime.strptime(member.date_of_birth, "%d-%m-%Y").month,
            datetime.strptime(member.date_of_birth, "%d-%m-%Y").day
        ), reverse=True)
        for member in living_members:
            age = datetime.now().year - datetime.strptime(member.date_of_birth, "%d-%m-%Y").year
            print(f"Tên: {member.name}, Tuổi: {age}, Ngày sinh: {member.date_of_birth}")

#Cau 8
    def count_members_by_gender(self, node=None):
        if node is None:
            node = self.root
        gender_count = {'Nam': 0, 'Nữ': 0}
        if node is not None:
            if node.gender == 'Nam':
                gender_count['Nam'] += 1
            elif node.gender == 'Nữ':
                gender_count['Nữ'] += 1
            if node.left:
                left_count = self.count_members_by_gender(node.left)
                gender_count['Nam'] += left_count['Nam']
                gender_count['Nữ'] += left_count['Nữ']
            if node.right:
                right_count = self.count_members_by_gender(node.right)
                gender_count['Nam'] += right_count['Nam']
                gender_count['Nữ'] += right_count['Nữ']
        return gender_count

#Cau 9
    def count_jobs(self, node=None):
        if node is None:
            node = self.root
        job_count = {}
        if node is not None:
            job_count[node.job] = job_count.get(node.job, 0) + 1
            if node.left:
                left_jobs = self.count_jobs(node.left)
                for job, count in left_jobs.items():
                    job_count[job] = job_count.get(job, 0) + count
            if node.right:
                right_jobs = self.count_jobs(node.right)
                for job, count in right_jobs.items():
                    job_count[job] = job_count.get(job, 0) + count
        return job_count
#Cau 10
    def _find_parent_node(self, node, name):
        if node is None:
            return None
        if node.left and node.left.name == name:
            return node, "left"
        elif node.right and node.right.name == name:
            return node, "right"
        else:
            found, side = self._find_parent_node(node.left, name)
            if found:
                return found, side
            return self._find_parent_node(node.right, name)
    def remove_person(self, name):
        if self.root.name == name:
            self.root = None
            return
        parent_node, side = self._find_parent_node(self.root, name)
        if parent_node:
            if side == "left":
                parent_node.left = None
            else:
                parent_node.right = None
        else:
            print("Không tìm thấy thành viên.")


# Sử dụng lớp FamilyTree
family_tree = FamilyTree()
# ... (thêm các thành viên vào cây)

while True:
    name = input("Nhập tên thành viên (hoặc 'kết thúc' để thoát): ")
    if name.lower() == 'kết thúc':
        break
    gender = input("Nhập giới tính (Nam/Nữ): ")
    birth_place = input("Nhập nơi sinh: ")
    date_of_birth = input("Nhập ngày sinh (dd-mm-yyyy): ")
    date_of_death = input("Nhập ngày mất (nếu còn sống thì bỏ trống): ")
    job = input("Nhập nghề nghiệp: ")

    person = Person(name, gender, birth_place, date_of_birth, date_of_death, job)
    parent_name = input("Nhập tên của cha/mẹ (nếu không có thì bỏ trống): ")
    family_tree.add_person(person, parent_name)

# In ra cây gia phả
family_tree.print_family_tree()

# Tìm kiếm thông tin thành viên
name_to_find = input("\nNhập tên thành viên cần tìm: ")
family_tree.find_person(name_to_find)

# Tính tổng số tuổi của các thành viên còn sống
total_age = family_tree.calculate_total_age_of_living_members()
print(f"\nTổng số tuổi của các thành viên còn sống trong gia phả là: {total_age}\n")

#In ra các thành viên không có con
family_tree.print_members_without_children()

# Nhập số đời N và in ra các thành viên thuộc đời đó
N = int(input("\nNhập số đời N để in ra các thành viên thuộc đời đó: "))
family_tree.print_members_of_generation(N)

#In ra các thành viên còn sống theo thứ tự từ lớn đến nhỏ
family_tree.print_living_members_sorted_by_age()

#thống kê ra các thành viên trong gia phả có giới tính Nam hoặc Nữ
gender_stats = family_tree.count_members_by_gender()
print(f"\nSố lượng thành viên giới tính Nam: {gender_stats['Nam']}")
print(f"Số lượng thành viên giới tính Nữ: {gender_stats['Nữ']}")

#Thống kê ra các nghề của các thành viên và nghề có nhiều thành viên nhất
job_stats = family_tree.count_jobs()
most_common_job = max(job_stats, key=job_stats.get)
print(f"\nCác nghề nghiệp và số lượng thành viên tương ứng: {job_stats}")
print(f"Nghề nghiệp có nhiều thành viên nhất: {most_common_job} ({job_stats[most_common_job]} thành viên)")

# Vòng lặp này cho phép bạn xóa nhiều thành viên. Nó chỉ dừng lại khi bạn nhập 'thoát'. Sau mỗi lần xóa, cây gia phả sẽ được in ra lại để bạn kiểm tra.
while True:
    name_to_remove = input("\nNhập tên thành viên cần xóa (hoặc 'thoát' để kết thúc): ")
    if name_to_remove.lower() == 'thoát':
        break
    family_tree.remove_person(name_to_remove)
    print(f"Đã xóa thành viên {name_to_remove} và con cháu.")
    print("\nCây gia phả sau khi xóa:")
    family_tree.print_family_tree()

