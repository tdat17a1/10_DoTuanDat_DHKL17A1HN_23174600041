import pandas as pd

# Bước 1: Đọc dữ liệu từ file euro2012.csv
euro12 = pd.read_csv('euro2012.csv')

# 1. In loại, hình dạng và danh sách các cột
print("\nLoại dữ liệu của euro12:", type(euro12))
print("Hình dạng của euro12:", euro12.shape)
print("Danh sách các cột của euro12:", euro12.columns.tolist())

# 2. In giá trị cột Goals
print("\nGiá trị cột Goals:\n", euro12['Goals'])

# 3. Số đội tham gia Euro 2012
num_teams = euro12['Team'].nunique()
print("Số đội tham gia Euro 2012:", num_teams)

# 4. In thông tin của Euro 2012
print("\nThông tin của Euro 2012:\n", euro12.info())

# 5. Tạo DataFrame discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]

# 6. Sắp xếp discipline giảm dần theo 'Red Cards' và 'Yellow Cards'
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print("\nDiscipline sau khi sắp xếp:\n", discipline_sorted)

# 7. Tính trung bình Yellow Cards
avg_yellow_cards = discipline['Yellow Cards'].mean()
print("\nTrung bình Yellow Cards:", avg_yellow_cards)

# 8. Lọc các đội đã ghi hơn 6 bàn thắng
teams_over_6_goals = euro12[euro12['Goals'] > 6]
print("\nCác đội đã ghi hơn 6 bàn thắng:\n", teams_over_6_goals)

# 9. In các đội có tên bắt đầu bằng 'G'
teams_starting_with_g = euro12[euro12['Team'].str.startswith('G')]
print("\nCác đội mà tên bắt đầu bằng 'G':\n", teams_starting_with_g)

# 10. In 7 cột đầu của euro12
print("\n7 cột đầu của euro12:\n", euro12.iloc[:, :7])

# 11. In tất cả các cột, trừ 3 cột cuối
print("\nTất cả các cột, trừ 3 cột cuối:\n", euro12.iloc[:, :-3])

# 12. In các cột 'Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards'
print("\nCác cột 'Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards':\n",
      euro12[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])

# 13. In các cột chỉ hiển thị 'Team', 'Shooting Accuracy' từ 'England', 'Italy', 'Russia'
teams_interest = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])]
print("\nCác cột 'Team' và 'Shooting Accuracy' từ 'England', 'Italy', 'Russia':\n",
      teams_interest[['Team', 'Shooting Accuracy']])
