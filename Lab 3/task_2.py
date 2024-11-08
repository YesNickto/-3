def find_common_participants(group1, group2, delimiter = "|"):
    group1_set = set(group1.split(delimiter))
    group2_set = set(group2.split(delimiter))
    common_participants = list(group1_set.intersection(group2_set))
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка с разделителем "|" (используется значение по умолчанию)
common = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common}")