# Project Technical Specification

## 1. Project Overview
### 1.1 Project Purpose
The goal is to build a web platform that allows users to create smart devices, drones, RC cars, automated irrigation systems, toys, etc. The platform will use AI at all stages and will guide the user from a simple prompt about what they want to create to a detailed product documentation including list of materials and electronic components required, wiring schematics, software if the device is using a microcontroller, 3d models ready to print, assembly instructions, and user manual. The platform will use blockchain to access AI computing power, AI models, pay for fine tuning and training, have a marketplace for designs, expertise, etc.

### 1.2 Problem Statement
Smart devices and electronic toys are the go to presents for most people and occupy a significant market. Hobbyists and DIY enthusiasts have been enjoying cheap access to electronics, sensors, 3d printers for quite a while and have proven that complex products could be created and assembled with a low budget and moderate skill level. We will lower the bar even more and allow anyone to create a custom device, tailored to his specifications. With the use of AI models, the whole process, from the idea to the technicals could be simplified a lot. From the choice of materials and components, picking the right parts and sensors, to designing the envelope for the assembled electronics, and the software running on it, it is currently possible to completely assist someone with very low expertise. On top of that, the platform will also offer a market for hobbyists and professionals to sell ready to go schematics, specially trained models, computing power for AI or their assembly expertise directly. The end user will have the ability to purchase software and wiring solutions, additional toolings or use more expensive AI models trained by experts to achieve better results. It will also be possible to get assisted by a human for any stage of the project through bounties, to have professionals solve or validate your project. People willing to make money on the platform could offer their assembly services in their own town, where anyone could pay them to assemble and deliver the end product to their homes directly. It will also be possible to ask someone near you to 3d print the parts you need for you and deliver them to you.

### 1.3 Target Users
#### People making toys for their kids
Always wanted to create that puzzle that you always thought would be a great toy? Maybe a rocket?
Want a cool DIY project to do with your kids?
Make that cool RC tank that shoots projectiles!

#### People making tailored presents
Build that soviet style clock your aunt always wanted
A smart device that helps you cook with the ingridients you have?

#### Startups wanting a prototype
Make that talking planter you always wanted to market
A new idea for a drone?
Want to make a better smart vacuum cleaner?
Create your own bluetooth speaker?
Self propelled roller blades? You got it!


#### Professionals with specific needs
You want a specific sensor for water salinity?
You think you can improve on automated irrigation systems?
Need smarter pest traps? Mosquito killing machines?
Create your own security devices


## 2. Technical Requirements
### 2.1 Technology Stack
- Frontend: Could be React, View, etc
- Backend: Nodejs, Nextjs, Rust, Go, etc
- Database: Mysql, Postgres, etc
- Other Tools: OpenAI, Cursor, etc

### 2.2 System Requirements
- Performance Requirements: TBD
- Scalability Requirements: TBD
- Security Requirements: TBD
- Compliance Requirements: TBD

## 3. Features and Functionality
### 3.1 Core Features
1. Custom project board
   - Description: Based on the first user input, build a project board with the required tools: Materials list, Wiring editor, 3d model editor, Coding assistant, Emulator
   - User Stories: The user creates a new project and enters a prompt describing what he wants to build, he then sees a project board with only the tools he will require for that project
   - Technical Requirements: A single user input is required, that will be directed to an AI serving as project orchestrator. The orchestrator must also provide more detailed specifications on the project that will be used by other AIs.

2. Materials selector
   - Description: The AI will prepare a broad list of generic materials and components required for the project
   - User Stories: After the project board is generated, the user sees the Material Editor component being populated by AI. Every material and component is described in a generic way, for example "DC Motor", "Spring", "Microcontroller" and has a list of properties decided by AI that could be voltage, size, power, diameter, anything the AI thinks is a good idea. The user can manually add materials and components, alter descriptions and properties at will. 
   - Technical Requirements: Items suggested by AI are marked "suggested", custom modifications and additions are marked "user". Suggested materials and components need to be validated by the user and then tagged "suggested, validated". AI must fill the Materials component as soon as the project board opens. The AI model picking the materials could be the global orchestrator model or a specific AI model that will be fed the project details. When user edits the materials, AI should check for coherence, for example voltage issues and either alert the user or provide a solution. For example if there is an issue with a power source that is too low voltage for the motor with a property of 5V voltage, the AI must suggest a step up component.

3. Shopping component
   - Description: For every material and component of the "materials component", the user can select a specific reference that matches the properties of the material.
   - User Stories: While working with the materials component, at any point a user can "shop" for a specific reference from a list that matches the properties assigned to the material or component. Once he picks a specific reference, the properties of the material or component are marked "resolved" if the reference matches the list of requirements. If the user edits the materials list and changes properties or picks a different reference, he gets incompatibility alerts if needed.
   - Technical Requirements: For every material, an AI should be used to list the compatible references. When a material property is altered a compatibility check must be ran on the whole project again, and provide alerts or solutions. Incompatible references, properties or materials should be marked clearly.

4. Wiring editor
   - Description: Upon request an AI will analyse the electronic components selected and generate a wiring diagram in the 2D wiring editor. It will take into account power, sensors, microcontrollers, motors, any electronics, in order to create a single device
   - User Stories: When all the components have a specific reference selected, the user can go into the Wiring editor and generate a wiring diagram. He can then edit the wiring diagram at will and see compatibility and consistency alerts when needed
   - Technical Requirements: AI will generate the wiring diagram for the editor, if user edits something manually, the diagram is sent back into the AI for validation. AI can return alerts, suggestions for fixes, etc

5. Assembly editor
   - Description: This is a 3d viewer that displays the materials and components and allows to place them and orient them at will. Components are also visible in a list next to the 3d viewer and allow for interaction with AI.
   - User Stories: The user can see his electronic components in 3D and place them precisely. In the components list he can select multiple components and ask AI to generate an attachment. The attachment is added between the objects and also as an element in the components tree. He can add that attachment as a Material to his Materials component. The user also created an envelope in the components tree. The user can edit any generated model by asking AI.
   - Technical Requirements: A specific AI must be used and fed with the components 3d models and wiring information to generate 3d printable parts. The editor is a 3d viewer with a 2d components tree for additional interaction such as with AI.

6. Code editor
   - Description: AI coding tooling. This could be platform-internal or outsourcing code edition and writing to IDEs like Cursor, VS Code, etc. The code editor writes the software that runs on the microcontroller if one is picked in the materials list. It handles proper communication with sensors, motors, etc based on the wiring schematics generated earlier.
   - User Stories: After his wiring schematics is done, the user opens the Code editor. He sees a library generated for his project that takes into account the GPIOs and other wiring information to pilot the components. Through prompts, he guides the AI into generating the software for this device. He can also select to export the project and work on it with the IDE of his choice, The platform is added to his github repository to see his commits so he make the AI validate his work in the platform later.

7. AI picker
   - Description: Allows the user to select between multiple AI models to use for every step: Orchestrator, Materials assistant, Shopping assistant, Wiring assistant, Coding assistant, 3D model assistant.
   - User Stories: The user wants to try the new wiring model, in his project he has access to a settings tab where he can edit the wiring model. The pricing model is displayed in the list of available wiring models.
   - Technical Requirements: A project settings tab must be built for user preferences. Possibly a generic settings tab that applies the user preferences to all of his projects. Backend must be aware of the possible choices for AI models.

8. Wallet
   - Description: The platform must be used with a crypto wallet that allows purchasing of the coin used to pay for services, view token price, monthly spending, subscriptions and one-off payments
   - Technical Requirements: The platform must operate using blockchain to purchase AI usage. Depending on AI providers, costs will be handled per-request, per-computing power, per-month, per-model, etc.

9. AI Marketplace
   - Description: Advanced actors can sell custom models, computing power, etc with different payment and subsription systems that will be used in the AI picker
   - Technical Requirements: Backend must implement on server level and on blockchain level the ability to provide and pay for services

10. Code Marketplace
   - Description: Libraries, Snippets and AI tools could be sold here to assist the end user in building the software for this project.
   - User Stories: The user can let AI generate the code to pilot his drone and spend computing resources and debugging time, or he could just pick a compatible solution that already exists and customize it. If he has an unusual component in his materials list, maybe a library written by someone is already available and AI compatible to drive his component, so the AI doesn't spend resources trying to write code to drive and debug that component.
   - Technical Requirements: Backend must implement on server level and on blockchain level the ability to handle (NFTs?) different kind of assets the user can purchase for his AI to use as help, guide, or implementation helps.

10. Bounties
   - Description: In case something is too complex for AI, the end user can create a bounty in hope that someone will solve his problem. Bounties can be asked for any stage of the project.
   - User Stories: The user can't figure out a wiring schematic for the components he picked. He creates a bounty using project tokens, selects what participants can see of his project and provides instructions and possible questions he has. The bounty gets published, and after a few hours he gets a submission where someone replaced one of his components with another compatible one, that makes the wiring schematics work. He can view the submission as a fork of his project with the changes, he can then accept the changes and the bounty gets paid and closed.
   - Technical Requirements: Create forks of projects with the ability to only see specific parts. A bounty project should behave in the same way as a normal project, but the bounty solver is the one who spends AI resources to work on the project. A system should be implemented to prevent the end user from copying the solution without paying the bounty.

11. Simulation
   - Description: For some microcontrollers, a simulator could be provided to help the user and AI to build the software. Most common electronic components could be included in the simulation, and Pro users could provide plugins to allow the simulation of more components and micro controllers.
   - Technical Requirements: Simulation tools are a product like the others, a simulation environment must be built that handles micro controllers, electronics, batteries, etc. An SDK must be provided to the pro users to develop plugins for the simulation tool in order to provide compatibility with electronic parts. For example a plugin could be implemented to handle a range of distance sensors for the raspberry pi. It would emulate distance data, power requirements and provide proper output on the simulated GPIOs of the raspberry.

### 3.2 User Workflows
#### End user Login
The user logs on the platform, he can see his wallet and the list of this project. He also sees the Marketplace component where he can see his purchases in terms of AI models, subsriptions, code snippets, libraries, etc. He can also see his bounties.
#### Pro user Login
The user logs on the platform. He can see a list of bounties to solve that he can respond to. He can also see his marketplace where his products are sold. He can see usage data for his products. If he provides AI models, he can see their daily usage. The user can also see assembly and 3d printing requests in his area.
#### End user project creation
The user creates a new project and sees a single prompt asking him to describe what he wants to build and the name of the project. He fills the prompt and the project name and clicks "Generate". Now is project has a dashboard with the proper tools he'll need, as well as access to prompting the Orchestrator AI. He can pick the AIs to use in the projects Settings tab.
#### End user project building
The user asks AI to generate the list of materials and components, he reviews and validates the list, adds missing elements if required, changes the properties of the elements in the list. For every change, the AI validates the consistency of his choices and flags issues and incompatibilites intil those are solved.
Once the materials and components list is complete and validated, the user picks specific references for every element in the list, AI provides him with lists of compatible references for every item, and at every selection validates once again the consistency.
Once the references for the components list are selected, the user goes into the Wiring component and AI generates a wiring proposal. The user can alter the wiring manually, while AI verifies his work and triggers alerts, warnings and issues and suggestions.
Once the wiring is done, the user moves to the 3d editor where he can place the components in a 3d view and assemble them using generated STL models. For the generated models, he can validate them and add them to his components list.
The user can chose to use the Code editor that is available once wiring is done, or he can chose to build the software himself
#### End user bounty creation
When facing with a difficulty, inability to solve the issues raised by AI, or confronted with limitations of AI assisted generation of materials, wiring, code or 3d models, the user creates a bounty and sets a reward. He can then follow his bounty and check for submissions. Submissions are in the form of forks of his project that he can view and validate to integrate the changes.
#### Pro user bounties
A user can see current bounties and chose to participate, he then sees a fork of the project to solve with a view limited to what the bounty creator selected. He can work on this project like the end user would, using the same toolings, or he can manually alter the project until the AIs validate the consistency of changes, or even overrule the AI by providing proper explanations. He then submits the fixed project and waits for reward.
#### Pro user marketplace
The user can submit a new product to the marketplace. The product can be in different categories such as:
- Tailored AI model: The user developed a model that is better suited for a specific stage of the project, he can submit his model on the marketplace and market the usage
- Computing Power: The user can sell computing power for this custom models or for other models on a per request bases or subscription model
- 3D models: The user can sell 3d printable models for will be available to end users when building their models: RC car bodies, Protection envolopes for microcontrollers, plastic screws and fixation mechanisms...
- Simulation plugins: Plugins to extend the simulator with new micro controllers, sensors, electronic components etc
- Libraries and code snippets: Code toolings tailored specifically to solve the most common tasks such as drone piloting, bluetooth communication, battery management etc
- Assembly of electronics: The user can be paid to acquire and assemble the electronic parts as per assembly and wiring instructions for the end user
- 3D printing: The user can perform 3d printing tasks for the end user

### 3.3 Integration Points
- Bittensor for AI requirements
- Blockchain for project token
- API libraries
- 3D toolings
- IDE integrations

## 4. Project Scope
### 4.1 Timeline
- Project Start Date: [September 2025]
- Key Milestones:
  1. Proof of concept [January 2026]
  2. Lightpaper [March 2026]
  3. Token sale [April 2026]
  4. Bittensor integration
  5. Alpha Release
  6. Simulation SDK
  7. Marketplace