#Importing modules
from flask import Flask, request, render_template

#Initializing the flask application
app = Flask(__name__,template_folder='template')

#Route for Home Page
#Root URL
@app.route('/')
#Function to handle requests to this endpoint.

def index():
    #Renders the index.html template, passing 'lot_size' and 'form_data' as context variables with initial values of None and an empty dictionary, respectively.
    return render_template('index.html', lot_size=None, form_data={})

#Route for Calculating Lot Size.
#Defines the URL endpoint for the calculation and specifies that it only accepts POST requests.
@app.route('/calculate', methods=['POST'])

#The function to handle requests to this endpoint.
def calculate():
    try:
        risk_amount = float(request.form['risk_amount'])
        commission_per_lot = float(request.form['commission_per_lot'])
        sl_size = float(request.form['sl_size'])
        lot_size = risk_amount / ((10 * sl_size) + commission_per_lot)
        lot_size = round(lot_size, 2)
        form_data = {
            'risk_amount': risk_amount,
            'commission_per_lot': commission_per_lot,
            'sl_size': sl_size
        }
        return render_template('index.html', lot_size=lot_size, form_data=form_data)
    
     #Handles cases where the input is not a valid float.
    except ValueError:
        form_data = {
            'risk_amount': request.form.get('risk_amount', ''),
            'commission_per_lot': request.form.get('commission_per_lot', ''),
            'sl_size': request.form.get('sl_size', '')
        }
        return render_template('index.html', lot_size="Invalid input. Please enter numerical values.", form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True)
