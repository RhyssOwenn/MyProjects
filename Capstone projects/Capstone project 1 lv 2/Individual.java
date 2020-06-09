package com.company;

public class Individual {
    String individualName;
    String individualAddress;
    String individualContact;
    String individualType;

    public String getIndividualName() {
        return individualName;
    }

    public String getIndividualAddress() {
        return individualAddress;
    }

    public String getIndividualContact() {
        return individualContact;
    }

    public String getIndividualType() {
        return individualType;
    }

    public String toString () {
        String output = "Name and surname: " + individualName;
        output += "\nAddress: " + individualAddress;
        output += "\nContact number: " + individualContact;
        output += "\nType of person: " + individualType;
        return output;
    }

    public Individual(String personName, String personAddress, String personContact, String personType) {
        this.individualName = personName;
        this.individualAddress = personAddress;
        this.individualContact = personContact;
        this.individualType = personType;
    }
}

