import csv
from faker import Faker
fake = Faker('uk_UA')

def pad_column(text, width):
    return f'{text:<{width}}'


def generate_personal_data_fixed_width(filename, num_records=2000):
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)


        column_widths = {
            'Прізвище': 15,
            'Ім’я': 12,
            'По батькові': 20,
            'Стать': 7,
            'Дата народження': 15,
            'Посада': 30,
            'Місто': 20,
            'Адреса': 35,
            'Телефон': 20,
            'Email': 30
        }

        # Заголовок таблиці з вирівнюванням
        header = [pad_column('Прізвище', column_widths['Прізвище']),
                  pad_column('Ім’я', column_widths['Ім’я']),
                  pad_column('По батькові', column_widths['По батькові']),
                  pad_column('Стать', column_widths['Стать']),
                  pad_column('Дата народження', column_widths['Дата народження']),
                  pad_column('Посада', column_widths['Посада']),
                  pad_column('Місто проживання', column_widths['Місто']),
                  pad_column('Адреса проживання', column_widths['Адреса']),
                  pad_column('Телефон', column_widths['Телефон']),
                  pad_column('Email', column_widths['Email'])]

        writer.writerow(header)

        for _ in range(num_records):
            gender = fake.random_element(elements=('male', 'female'))
            last_name = fake.last_name_male() if gender == 'male' else fake.last_name_female()
            first_name = fake.first_name_male() if gender == 'male' else fake.first_name_female()
            patronymic = fake.middle_name_male() if gender == 'male' else fake.middle_name_female()
            birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
            position = fake.job()
            city = fake.city()
            address = fake.address()
            phone = fake.phone_number()
            email = fake.email()

            # Запис рядка з вирівнюванням
            row = [pad_column(last_name, column_widths['Прізвище']),
                   pad_column(first_name, column_widths['Ім’я']),
                   pad_column(patronymic, column_widths['По батькові']),
                   pad_column(gender, column_widths['Стать']),
                   pad_column(birth_date.strftime('%Y-%m-%d'), column_widths['Дата народження']),
                   pad_column(position, column_widths['Посада']),
                   pad_column(city, column_widths['Місто']),
                   pad_column(address, column_widths['Адреса']),
                   pad_column(phone, column_widths['Телефон']),
                   pad_column(email, column_widths['Email'])]

            writer.writerow(row)



generate_personal_data_fixed_width('personal_data.csv', 2001)
