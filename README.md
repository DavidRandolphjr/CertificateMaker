# Certificate Maker
This application was created to simplify the certificate making process for my family's insurance business. For whatever reason, Erie Insurance still requires the use of the retired internet explorer in order to generate an insurance certificate. This means that once you generate the certificate in a modern browser, you must save the adobe link,
open the edge browser in internet explore compatibility mode, enter your credentials for erie's website, pass the two step verification, navigate to the adobe link, download the file, open in adobe acrobat, sign input your signature, save, and email. For me, this was way too many steps. With this new application, you simply enter the required information
for the certificate, click save, then email.

# How it Works
Utilizing Python and Tkinter, I created an application that takes user input to autofill a certificate pdf. If the user does not know how to fill out the certificate, I simplified the process further by allowing the user to upload specific insurance pdf files so that the Tkinter app can scrape the file for the information needed. Once finished, the user can save the
entry to make the process easier for the next time. I omitted the required pdf files for safety.
