import streamlit as st
from PIL import Image

def main():
    '''building biometric fingerprint login'''

    menu = ['Home', 'Login']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':

        st.title('DATAQUEST')
        st.write('Motivation and oppourtunity creation has been the key role of Dataquest.'
                 ' Due to this , our team came up with a  one month challenge where our students are given opportunity'
                 'to particepate in unguided projects and submit to  DQ community. '
                 'We had 5 projects  that were to be done  that is;  Analysis of Covid 19, Using Machine Learning ein Titanic Survval'
                 ',Explore any Site and give the best time to  post and state out clearly what  type of post to have,Explore on World Population,'
                 'Explore on eBay used car.'
                 'Since this  attracted many students, we devided our awards into 4 categories;'
                 '1) the first three winneners to be awarded  490 dollars, the 2) the second category to be awarded one month free subscriptions, 3) '
                 'third category to be awarded a certificate and website and the 4)  category to be awarded one week learning free.'
                 ''
                 'Remember the second and fist category enjoy the third awards.'
                 ''
                 'In all the category Awards, we have four of our moderators who will check and recommend on who to be awarded. '
                 ''
                 ''
                 'For the website , the four moderators have been given  26 students each and ensure the complition of the  website by 10th.'
                 ''
                 'The winner shall be announced on 8th .'
                 ''
                 'Below is a sample of our certificate.'
                 
                 
                 '')


        image = Image.open('student.PNG')

        st.image(image, caption='Authorized by DataQuest',output_format="auto'")

        st.write('Note: This section is only available to the students who have qualified for the certificates  and the website, you '
                 'will not be in a postion to  save your certificate if you have not meet the minumum qualification that is, payement of 8 dollars and '
                 'complition of any of the project mentioned above')

    elif choice=='Login':
        st.subheader('Login Section')
        name=st.text_input('Enter your full names here')
        email=st.text_input('Enter your email address')
        username=st.text_input('User Name')
        password = st.text_input('Password',type='password')
        passw=['1234','1rts']
        if st.checkbox('Login'):
            if name:
                if password == 'LR53':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('martin.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'S4JJ':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('ann.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'DX5W':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('purity.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'UGET':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('gracie.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'R7B2':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('grace.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))

                elif password == '27F3':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('boniface.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'SE8UU':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('herbert.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))

                elif password == 'ELSY':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('ernest.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'YPON':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('nelly.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == '5598':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('ruth.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'R20R':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('ogutu.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'GVR4':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('leshan.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == '1N9U':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('toel.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'X5QR':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('fedelis.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'EFWG':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('zipporah.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'ZNQL':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('david.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'OGCN':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('gailey.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'OPVI':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('vaati.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'BRFK':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('francis.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'ODTI':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails.'
                                                                                     'Also take note that your particepation  has increases your chances of '
                                                                                     'being given a six month schollarship.')
                    image = Image.open('defao.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                elif password == 'MNQR':
                    st.success('You have successfully Logged in as {}!'.format(name)+' Your website is underway and  you shall be '
                                                                                         'notified in due course. We thank you for particepating in the challenge '
                                                                                         'and keep in touch with our moderators for the upcoming events. '
                                                                                         'You can Write click on the image to save your certiicate.'
                                                                                     'Final announcement is on 8th, so keep in touch with your emails')
                    image = Image.open('lewis.PNG')

                    st.image(image, caption='Keep Moving', output_format="auto'")

                    st.write('Happy Coding {}!'.format(username))
                else:
                    st.warning('Kindly ensure you entered the correct code, your password can not match any value in our system.')








if __name__== '__main__':
    main()