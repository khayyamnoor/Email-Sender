import smtplib
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox

def message():

    user_email= email_entry.get()
    mail = text.get("1.0",'end-1c')

    email = EmailMessage()
    email['from'] = 'Khayyam Noor'
    email['to'] = user_email
    email['subject'] = 'You have recieved an Email'
    email.set_content(mail)
    #connect to the server
    with smtplib.SMTP(host='smtp.gmail.com' , port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('dummieacc792@gmail.com' , 'kswamwksbxphzgre') #credentials
        smtp.send_message(email) #stuff we have written in the email
        print('Email Sent Succesfully')#to check if coderuns in the terminal
        my_label.config(text="Email Sent Succesfully")
# ---------------------------------------------------------------------------------

window = Tk()
window.title("Email Buddy")
window.configure(bg='white')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="4302_1362187600_g5.png")
canvas.create_image(100, 100, image=logo_img)
canvas.config(borderwidth=0,bd=0, highlightthickness=0)
canvas.grid(row=0, column=1)
# labels

email_label = Label(text="Email/Username:")
email_label.configure(bg='white')
email_label.grid(row=2, column=0)

my_label=Label(font=('Arial', 20, "bold"))
my_label.pack
my_label.config(text="",bg="white")

my_label.grid(row=5, column=1)

email_body = Label(text="Email Body:")
email_body.configure(bg='white')
email_body.grid(row=3, column=0)

# Entry
email_entry = Entry(width=36)
email_entry.insert(0,"admin@gmail.com")
email_entry.grid(row=2, column=1)

# Button
search_button = Button(text="Send Email", command=message)
search_button.config(width=10, padx=15,bg='white')
search_button.grid(row=4, column=2, columnspan=3)
# Text Field
quote='''Dear Sir/ Madam 
Hi there,\n
Thank you for your email. I will be out of the office from 5/12 to 6/15 and will have limited access to email / will not have access to email.\n
If this is urgent, please contact Mr.Dennis at denis122@hotmail.com or 9284-555-889.\n
I will do my best to respond promptly to your email when I return on 16/20.\n

Best regards,\n

Your Name.'''
text = Text()
text.config(height=19,width=36)
text.insert(INSERT, quote)
# text.insert(END, "Bye Bye.....")
text.grid(row=3, column=1)

window.mainloop()