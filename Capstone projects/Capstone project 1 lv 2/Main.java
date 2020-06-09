package com.company;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        //Declare variable names for project
        String projectNumber;
        String projectName;
        String projectType;
        String projectAddress;
        String projectErfNumber;
        float projectFee;
        float feePaid;
        String projectDeadline;

        //Declare variables names for individual
        String individualName;
        String individualAddress;
        String individualContact;
        String individualType;

        //Declare variable names for program
        int menuNav = 0;

        while (menuNav != 99) {
            //Create main menu
            System.out.println("Select an option by typing the corresponding number:");
            System.out.println("1. Add person");
            System.out.println("2. Add project");
            System.out.println("3. Edit project");
            System.out.println("4. Exit");
            menuNav = input.nextInt();

            //if user chooses 1. Add an individual.
            if(menuNav == 1) {
                System.out.println("\nAdd new person");
                System.out.println("\nName and Surname:" + input.nextLine());
                individualName = input.nextLine();
                System.out.println("Address:");
                individualAddress = input.nextLine();
                System.out.println("Contact number:");
                individualContact = input.nextLine();
                System.out.println("Person title:");
                individualType = input.nextLine();

                Individual individual = new Individual(individualName, individualAddress, individualContact, individualType);
                System.out.println("\n" + individual + "\n");
            }

            //if user chooses 2. Add new project.
            if(menuNav == 2) {
                System.out.println("\nAdd new Project:");
                System.out.println("Project Number: " + input.nextLine());
                projectNumber = input.nextLine();
                System.out.println("Project Name: ");
                projectName = input.nextLine();
                System.out.println("Project Type: ");
                projectType = input.nextLine();
                System.out.println("Project Address: ");
                projectAddress = input.nextLine();
                System.out.println("Project Erf Number:");
                projectErfNumber = input.nextLine();
                System.out.println("Total Cost: ");
                projectFee = input.nextFloat();
                System.out.println("Already paid: ");
                feePaid = input.nextFloat();
                System.out.println("Project Deadline: " + input.nextLine());
                projectDeadline = input.nextLine();

                Project project = new Project (projectNumber, projectName, projectType, projectAddress, projectErfNumber, projectFee, feePaid, projectDeadline);
                System.out.println("\n" + project + "\n");
            }
            // if user chooses 3. Edit project
            if(menuNav == 3) {
                System.out.println("\nEdit Project:");
                System.out.println(Project); //How can i call the project class so that the projects are listed for user?
                System.out.println("\nType the number of the project you would like to edit: ");
                //Could do with some help on how to go about editing the project.

            }
            //if user chooses 4. Exit.
            if(menuNav == 4) {
                System.out.println("You have now quit.");
                input.close();
            }
        }

        System.out.println("You have now quit.");
        input.close();
    }
}
