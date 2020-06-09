package com.company;

public class Project {
    String projectNumber;
    String projectName;
    String projectType;
    String projectAddress;
    String projectErfNumber;
    float projectFee;
    float feePaid;
    String projectDeadline;

    //Method
    public String getProjectNumber () {
        return projectNumber;
    }

    public String getProjectName () {
        return projectName;
    }

    public String getProjectType() {
        return projectType;
    }

    public String getProjectAddress() {
        return projectAddress;
    }

    public String getProjectErfNumber() {
        return projectErfNumber;
    }

    public float getProjectFee() {
        return projectFee;
    }

    public float getFeePaid() {
        return feePaid;
    }

    public String getProjectDeadline() {
        return projectDeadline;
    }

    public String toString () {
        String output = "Project number: " + projectNumber;
        output += "\nProject name: " + projectName;
        output += "\nProject type: " + projectType;
        output += "\nProject address: " + projectAddress;
        output += "\nErf number: " + projectErfNumber;
        output += "\nProject fee: " + projectFee;
        output += "\nProject address: " + feePaid;
        output += "\nProject deadline: " + projectDeadline;
        return output;
    }

    //Constructor
    public Project(String projectNumber, String projectName, String projectType, String projectAddress, String erfNumber, float projectFee, float feePaid, String projectDeadline) {
        this.projectNumber = projectNumber;
        this.projectName = projectName;
        this.projectType = projectType;
        this.projectAddress = projectAddress;
        this.projectErfNumber = erfNumber;
        this.projectFee = projectFee;
        this.feePaid = feePaid;
        this.projectDeadline = projectDeadline;
    }
}




