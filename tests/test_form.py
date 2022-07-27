import os
from selene.support.shared import browser
from selene import have
from faker import Faker


def test_form():
    fake = Faker()

    browser.open('/automation-practice-form')

    name = fake.first_name()
    browser.element('#firstName').type(name)

    lastname = fake.last_name()
    browser.element('#lastName').type(lastname)

    email = fake.free_email()
    browser.element('#userEmail').type(email)

    browser.element('#genterWrapper').all('.custom-radio').element_by(have.exact_text('Male')).click()

    phone_number = str(fake.random_number(digits=10))
    browser.element('#userNumber').type(phone_number)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1993"]').click()
    browser.element('.react-datepicker__month-select [value="5"]').click()
    browser.element('.react-datepicker__day--011').click()

    browser.element('#subjectsInput').type('Commerce').press_enter()

    browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
    browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    browser.element("#uploadPicture").send_keys(os.path.abspath('../src/images/kote.jpeg'))

    address = fake.street_address()
    browser.element('#currentAddress').type(address)
    browser.element('#state').element('input').type('NCR').press_enter()
    browser.element('#city').element('input').type('Noida').press_enter()

    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all('.modal-dialog').all('table tr')[1].all('td').should(have.exact_texts('Student Name', f'{name} {lastname}'))
    browser.all('.modal-dialog').all('table tr')[2].all('td').should(have.exact_texts('Student Email', email))
    browser.all('.modal-dialog').all('table tr')[3].all('td').should(have.exact_texts('Gender', 'Male'))
    browser.all('.modal-dialog').all('table tr')[4].all('td').should(have.exact_texts('Mobile', phone_number))
    browser.all('.modal-dialog').all('table tr')[5].all('td').should(have.exact_texts('Date of Birth', '11 June,1993'))
    browser.all('.modal-dialog').all('table tr')[6].all('td').should(have.exact_texts('Subjects', 'Commerce'))
    browser.all('.modal-dialog').all('table tr')[7].all('td').should(have.exact_texts('Hobbies', 'Sports, Reading, '
                                                                                                 'Music'))
    browser.all('.modal-dialog').all('table tr')[8].all('td').should(have.exact_texts('Picture', 'kote.jpeg'))
    browser.all('.modal-dialog').all('table tr')[9].all('td').should(have.exact_texts('Address', address))
    browser.all('.modal-dialog').all('table tr')[10].all('td').should(have.exact_texts('State and City', 'NCR '
                                                                                                         'Noida'))
