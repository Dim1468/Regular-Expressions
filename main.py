import csv
from pprint import pprint
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
def union_contact(contacts: list):
    result_list = []
    seen = set()

    for contact in contacts:
        key = (contact[0], contact[1])
        if key not in seen:
            result_list.append(contact)
            seen.add(key)
        else:
            existing_contact = next((c for c in result_list if (c[0], c[1]) == key), None)
            for i in range(2, len(contact)):
                if existing_contact[i] == '' and contact[i] != '':
                    existing_contact[i] = contact[i]

    return result_list


def create_contact(contact_list: list):
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7-(\2) \3-\4-\5'
    new_list = list()
    for item in contact_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  re.sub(phone_pattern, phone_substitution, item[5]),
                  item[6]]
        new_list.append(result)
    return union_contact(new_list)


pprint(create_contact(contacts_list))
Changed_list= create_contact(contacts_list)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(Changed_list)
