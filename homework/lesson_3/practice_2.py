def user_info(name, surname, birth_year, city, email, phone):
    return f"{surname} {name}, {birth_year} года рождения, г. {city}, email {email}, тел. {phone}"


print(user_info(name="Tom", birth_year="1979", city="Moscow", email="tm@me.com", phone="+767857544", surname="Hanks"))