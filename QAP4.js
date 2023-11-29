// Andrew Hannaford

const motelCust = {
  nameF: 'Andrew',
  nameL: 'Hannaford',
  birthDate: '07/03/1998',
  gender: 'Male',
  roomPreferences: ['standard', 'ocean view', 'poolside', '2 beds'],
  paymentMethod: 'Cash', 
  numberOfGuests: 3 ,
  mailingAdd: {
    city: 'Mount Pearl', 
    street: '12 ABC street',
    postal: 'X9X 9X9'
  },
  checkIn: '11/26/2023',
  checkOut: {
    time: '12:00PM',
    date: '11/30/2023',
  },

  getStay: function(){
        const checkInDate = new Date(this.checkIn);
        const checkOutDate = new Date(this.checkOut.date);
        const durationInMilliseconds = checkOutDate - checkInDate;
        const durationInDays = durationInMilliseconds / (1000 * 60 * 60 * 24);
        return durationInDays;
    },
  calculateAge: function() {
    const birthYear = parseInt(this.birthDate.split('/')[2]);
    const currentYear = new Date().getFullYear();
    return currentYear - birthYear;
  },
}

const customerDescription = `
  Customer Information:
  Name: ${motelCust.nameF} ${motelCust.nameL}
  Age: ${motelCust.calculateAge()} years old
  Gender: ${motelCust.gender}
  Room Preferences: ${motelCust.roomPreferences.join(', ')}
  Payment Method: ${motelCust.paymentMethod}
  Number of Guests: ${motelCust.numberOfGuests}
  Mailing Address: 
    City: ${motelCust.mailingAdd.city}
    Street: ${motelCust.mailingAdd.street}
    Postal Code: ${motelCust.mailingAdd.postal}
  Check-in Date: ${motelCust.checkIn}
  Check-out Date: ${motelCust.checkOut.date}
  Duration of Stay: ${motelCust.getStay()} days
`;

console.log(customerDescription);
