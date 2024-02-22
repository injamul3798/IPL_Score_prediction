from django.shortcuts import render, HttpResponse
from .forms import ModelForm
import pickle
import pandas as pd

# Load the model (consider loading it outside the view function if it's resource-intensive)
model = pickle.load(open('F:\\scorePrediction\\MLcode\\best_model.pkl', 'rb'))

def home(request):
    form = ModelForm()
    return render(request, 'cform.html', {'form': form})

def preprocess_data(venue, bat_team, bowl_team, batsman, bowler):
    venueName = {
    "M Chinnaswamy Stadium": 0,
    "Punjab Cricket Association Stadium, Mohali": 1,
    "Feroz Shah Kotla": 2,
    "Wankhede Stadium": 3,
    "Eden Gardens": 4,
    "Sawai Mansingh Stadium": 5,
    "Rajiv Gandhi International Stadium, Uppal": 6,
    "MA Chidambaram Stadium, Chepauk": 7,
    "Dr DY Patil Sports Academy": 8,
    "Newlands": 9,
    "St George's Park": 10,
    "Kingsmead": 11,
    "SuperSport Park": 12,
    "Buffalo Park": 13,
    "New Wanderers Stadium": 14,
    "De Beers Diamond Oval": 15,
    "OUTsurance Oval": 16,
    "Brabourne Stadium": 17,
    "Sardar Patel Stadium, Motera": 18,
    "Barabati Stadium": 19,
    "Vidarbha Cricket Association Stadium, Jamtha": 20,
    "Himachal Pradesh Cricket Association Stadium": 21,
    "Nehru Stadium": 22,
    "Holkar Cricket Stadium": 23,
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium": 24,
    "Subrata Roy Sahara Stadium": 25,
    "Shaheed Veer Narayan Singh International Stadium": 26,
    "JSCA International Stadium Complex": 27,
    "Sheikh Zayed Stadium": 28,
    "Sharjah Cricket Stadium": 29,
    "Dubai International Cricket Stadium": 30,
    "Maharashtra Cricket Association Stadium": 31,
    "Punjab Cricket Association IS Bindra Stadium, Mohali": 32,
    "Saurashtra Cricket Association Stadium": 33,
    "Green Park": 34,
    }

    venue = venueName.get(venue, 0)

    
    batTeam = {
    'Kolkata Knight Riders': 0,
    'Chennai Super Kings': 1,
    'Rajasthan Royals': 2,
    'Mumbai Indians': 3,
    'Deccan Chargers': 4,
    'Kings XI Punjab': 5,
    'Royal Challengers Bangalore': 6,
    'Delhi Daredevils': 7,
    'Kochi Tuskers Kerala': 8,
    'Pune Warriors': 9,
    'Sunrisers Hyderabad': 10,
    'Rising Pune Supergiants': 11,
    'Gujarat Lions': 12,
    'Rising Pune Supergiant': 13
    }
    bat_team = batTeam.get(bat_team, 0)

    
    bowlTeam = {
    'Royal Challengers Bangalore': 0,
    'Kings XI Punjab': 1,
    'Delhi Daredevils': 2,
    'Kolkata Knight Riders': 3,
    'Rajasthan Royals': 4,
    'Mumbai Indians': 5,
    'Chennai Super Kings': 6,
    'Deccan Chargers': 7,
    'Pune Warriors': 8,
    'Kochi Tuskers Kerala': 9,
    'Sunrisers Hyderabad': 10,
    'Rising Pune Supergiants': 11,
    'Gujarat Lions': 12,
    'Rising Pune Supergiant': 13
    }
    bowl_team = bowlTeam.get(bowl_team, 0)

    
    batsMan = {
    'SC Ganguly': 0,
    'BB McCullum': 1,
    'RT Ponting': 2,
    'DJ Hussey': 3,
    'Mohammad Hafeez': 4,
    'PA Patel': 5,
    'ML Hayden': 6,
    'MEK Hussey': 7,
    'MS Dhoni': 8,
    'SK Raina': 9,
    'JDP Oram': 10,
    'S Badrinath': 11,
    'T Kohli': 12,
    'YK Pathan': 13,
    'SR Watson': 14,
    'M Kaif': 15,
    'DS Lehmann': 16,
    'RA Jadeja': 17,
    'M Rawat': 18,
    'D Salunkhe': 19,
    'SK Warne': 20,
    'SK Trivedi': 21,
    'L Ronchi': 22,
    'ST Jayasuriya': 23,
    'DJ Thornely': 24,
    'RV Uthappa': 25,
    'PR Shah': 26,
    'AM Nayar': 27,
    'SM Pollock': 28,
    'Harbhajan Singh': 29,
    'AC Gilchrist': 30,
    'Y Venugopal Rao': 31,
    'VVS Laxman': 32,
    'A Symonds': 33,
    'RG Sharma': 34,
    'SB Styris': 35,
    'AS Yadav': 36,
    'SB Bangar': 37,
    'WPUJC Vaas': 38,
    'RP Singh': 39,
    'K Goel': 40,
    'JR Hopes': 41,
    'KC Sangakkara': 42,
    'DPMD Jayawardene': 43,
    'Yuvraj Singh': 44,
    'IK Pathan': 45,
    'S Sohal': 46,
    'B Lee': 47,
    'PP Chawla': 48,
    'WA Mota': 49,
    'Shahid Afridi': 50,
    'RR Sarwan': 51,
    'S Sreesanth': 52,
    'VRV Singh': 53,
    'S Chanderpaul': 54,
    'R Dravid': 55,
    'LRPL Taylor': 56,
    'JH Kallis': 57,
    'V Kohli': 58,
    'MV Boucher': 59,
    'P Kumar': 60,
    'SB Joshi': 61,
    'Z Khan': 62,
    'R Vinay Kumar': 63,
    'WP Saha': 64,
    'LR Shukla': 65,
    'AB Agarkar': 66,
    'M Kartik': 67,
    'I Sharma': 68,
    'AM Rahane': 69,
    'DJ Bravo': 70,
    'MA Khote': 71,
    'G Gambhir': 72,
    'V Sehwag': 73,
    'S Dhawan': 74,
    'Shoaib Malik': 75,
    'MK Tiwary': 76,
    'KD Karthik': 77,
    'R Bhatia': 78,
    'MF Maharoof': 79,
    'VY Mahesh': 80,
    'DB Das': 81,
    'HH Gibbs': 82,
    'DNT Zoysa': 83,
    'D Kalyankrishna': 84,
    'GC Smith': 85,
    'SA Asnodkar': 86,
    'Sohail Tanvir': 87,
    'SP Fleming': 88,
    'S Vidyut': 89,
    'JA Morkel': 90,
    'LPC Silva': 91,
    'DB Ravi Teja': 92,
    'SE Marsh': 93,
    'YV Takawale': 94,
    'SS Tiwary': 95,
    'RR Raje': 96,
    'Joginder Sharma': 97,
    'MS Gony': 98,
    'M Muralitharan': 99,
    'M Ntini': 100,
    'W Jaffer': 101,
    'CL White': 102,
    'Misbah-ul-Haq': 103,
    'DT Patil': 104,
    'A Kumble': 105,
    'DW Steyn': 106,
    'S Anirudha': 107,
    'MM Patel': 108,
    'AB de Villiers': 109,
    'A Chopra': 110,
    'BJ Hodge': 111,
    'T Taibu': 112,
    'Umar Gul': 113,
    'PP Ojha': 114,
    'SP Goswami': 115,
    'B Akhil': 116,
    'Salman Butt': 117,
    'TM Dilshan': 118,
    'A Mishra': 119,
    'J Arunkumar': 120,
    'Iqbal Abdulla': 121,
    'CK Kapugedera': 122,
    'LA Pomersbach': 123,
    'Shoaib Akhtar': 124,
    'AB Dinda': 125,
    'SR Tendulkar': 126,
    'AB Dinda': 127,
    'SR Tendulkar': 128,
    'B Chipli': 129,
    'DR Smith': 130,
    'SD Chitnis': 131,
    'Kamran Akmal': 132,
    'TM Srivastava': 133,
    'MK Pandey': 134,
    'RR Powar': 135,
    'JP Duminy': 136,
    'JD Ryder': 137,
    'KP Pietersen': 138,
    'CH Gayle': 139,
    'MC Henriques': 140
    
    }
    batsman = batsMan.get(batsman, 0)
    
    bowlerName = {
    'P Kumar': 0,
    'Z Khan': 1,
    'AA Noffke': 2,
    'JH Kallis': 3,
    'SB Joshi': 4,
    'CL White': 5,
    'B Lee': 6,
    'S Sreesanth': 7,
    'JR Hopes': 8,
    'IK Pathan': 9,
    'K Goel': 10,
    'PP Chawla': 11,
    'WA Mota': 12,
    'GD McGrath': 13,
    'B Geeves': 14,
    'MF Maharoof': 15,
    'R Bhatia': 16,
    'DL Vettori': 17,
    'R Vinay Kumar': 18,
    'B Akhil': 19,
    'AB Dinda': 20,
    'I Sharma': 21,
    'AB Agarkar': 22,
    'M Kartik': 23,
    'Mohammad Hafeez': 24,
    'DJ Hussey': 25,
    'MM Patel': 26,
    'SR Watson': 27,
    'SK Trivedi': 28,
    'SK Warne': 29,
    'D Salunkhe': 30,
    'Pankaj Singh': 31,
    'YK Pathan': 32,
    'Mohammad Asif': 33,
    'VY Mahesh': 34,
    'SM Pollock': 35,
    'A Nehra': 36,
    'DS Kulkarni': 37,
    'Harbhajan Singh': 38,
    'DJ Bravo': 39,
    'VS Yeligati': 40,
    'AM Nayar': 41,
    'MA Khote': 42,
    'Sohail Tanvir': 43,
    'JDP Oram': 44,
    'MS Gony': 45,
    'P Amarnath': 46,
    'M Muralitharan': 47,
    'Joginder Sharma': 48,
    'RP Singh': 49,
    'DNT Zoysa': 50,
    'SB Bangar': 51,
    'Shahid Afridi': 52,
    'PP Ojha': 53,
    'D Kalyankrishna': 54,
    'VRV Singh': 55,
    'Yuvraj Singh': 56,
    'DW Steyn': 57,
    'CRD Fernando': 58,
    'ST Jayasuriya': 59,
    'V Kohli': 60,
    'Gagandeep Singh': 61,
    'Umar Gul': 62,
    'SC Ganguly': 63,
    'LR Shukla': 64,
    'PJ Sangwan': 65,
    'Shoaib Malik': 66,
    'V Sehwag': 67,
    'A Kumble': 68,
    'DP Vijaykumar': 69,
    'SB Styris': 70,
    'RR Raje': 71,
    'JA Morkel': 72,
    'L Balaji': 73,
    'CK Kapugedera': 74,
    'DR Smith': 75,
    'WPUJC Vaas': 76,
    'Y Venugopal Rao': 77,
    'AD Mascarenhas': 78,
    'A Mishra': 79,
    'DJ Thornely': 80,
    'PM Sarvesh Kumar': 81,
    'Abdur Razzak': 82,
    'TM Dilshan': 83,
    'SD Chitnis': 84,
    'M Ntini': 85,
    'RR Powar': 86,
    'SK Raina': 87,
    'BAW Mendis': 88,
    'T Thushara': 89,
    'A Flintoff': 90,
    'Kamran Khan': 91,
    'T Henderson': 92,
    'FH Edwards': 93,
    'Harmeet Singh': 94,
    'KP Pietersen': 95,
    'LRPL Taylor': 96,
    'JD Ryder': 97,
    'Anureet Singh': 98,
    'CH Gayle': 99,
    'RR Bose': 100,
    'YA Abdulla': 101,
    'RS Bopara': 102,
    'SL Malinga': 103,
    'DP Nannes': 104,
    'RG Sharma': 105,
    'Shoaib Ahmed': 106,
    'BJ Hodge': 107,
    'RA Jadeja': 108,
    'RE van der Merwe': 109,
    'KP Appanna': 110,
    'JP Duminy': 111,
    'SR Tendulkar': 112,
    'VS Malik': 113,
    'SM Harwood': 114,
    'AS Raut': 115,
    'D du Preez': 116,
    'RJ Harris': 117,
    'TL Suman': 118,
    'A Singh': 119,
    'M Morkel': 120,
    'LA Carseldine': 121,
    'S Tyagi': 122,
    'SB Jakati': 123,
    'A Mithun': 124,
    'AM Rahane': 125,
    }
    bowler = bowlerName.get(bowler, 0)
    
    # Ensure the order of columns matches exactly with the model's expectations
    columns = ['venue', 'bat_team', 'bowl_team', 'batsman', 'bowler']
    data = [[venue, bat_team, bowl_team, batsman, bowler]]
    return pd.DataFrame(data, columns=columns)

def result(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            venue = form.cleaned_data['venue_choices']
            bat_team = form.cleaned_data["batting_team_choices"]
            bowl_team = form.cleaned_data["bowling_team_choices"]
            batsman = form.cleaned_data["striker_choices"]
            bowler = form.cleaned_data["bowler_choices"]

            input_data = preprocess_data(venue, bat_team, bowl_team, batsman, bowler)

            prediction = model.predict(input_data)

            context = {
                'input_data': {
                    'venue': venue,
                    'bat_team': bat_team,
                    'bowl_team': bowl_team,
                    'batsman': batsman,
                    'bowler': bowler
                },
                'predicted_runs': prediction[0]
            }

            return render(request, 'result.html', context)
        else:
            return HttpResponse("Form is not valid; please check the input data.")
    else:
        return HttpResponse('This page expects a POST request.')




'''from django.shortcuts import render, HttpResponse
from prediction.forms import ModelForm
import pickle
import pandas as pd

# Load the model (consider loading it outside the view function if it's resource-intensive)
model = pickle.load(open('F:\\scorePrediction\\random_forest_model.pkl', 'rb'))

from django.shortcuts import render
from .forms import ModelForm

def home(request):
    form = ModelForm()  # Initialize an instance of the form
    return render(request, 'cform.html', {'form': form})

def preprocess_data(venue, bat_team, bowl_team, batsman, bowler):
    venueName = {'M Chinnaswamy Stadium': 0, 'Punjab Cricket Association Stadium, Mohali': 1}
    venue = venueName.get(venue, 0)
    
    batTeam = {'Kolkata Knight Riders': 0, 'Chennai Super Kings': 1}
    bat_team = batTeam.get(bat_team, 0)
    
    bowlTeam = {'Royal Challengers Bangalore': 0, 'Kings XI Punjab': 1}
    bowl_team = bowlTeam.get(bowl_team, 0)
    
    batsMan = {'SC Ganguly': 0, 'BB McCullum': 1}
    batsman = batsMan.get(batsman, 0)
    
    bowlerName = {'P Kumar': 0, 'Z Khan': 1}
    bowler = bowlerName.get(bowler, 0)
    
    # Ensure the order of columns matches exactly with the model's expectations
    columns = ['venue', 'bat_team', 'bowl_team', 'batsman', 'bowler']
    data = [[venue, bat_team, bowl_team, batsman, bowler]]
    return pd.DataFrame(data, columns=columns)

def result(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            # Extracting form data
            venue = form.cleaned_data['venue']
            bat_team = form.cleaned_data["bat_team"]
            bowl_team = form.cleaned_data["bowl_team"]
            batsman = form.cleaned_data["batsman"]
            bowler = form.cleaned_data["bowler"]

            # Preprocessing the input data
            input_data = preprocess_data(venue, bat_team, bowl_team, batsman, bowler)

            # Making predictions
            prediction = model.predict(input_data)

            # Building the context for the template
            context = {
                'input_data': {
                    'venue': venue,
                    'bat_team': bat_team,
                    'bowl_team': bowl_team,
                    'batsman': batsman,
                    'bowler': bowler
                },
                'predicted_runs': prediction[0]  # Assuming prediction is a single value
            }

            # Rendering the template with context
            return render(request, 'result.html', context)
        else:
            return HttpResponse("Form is not valid; please check the input data.")
    else:
        return HttpResponse('This page expects a POST request.')'''

