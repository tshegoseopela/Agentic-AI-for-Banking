# Claims Agent Demo
This watsonx Orchestrate agent shows how to set up and run a simple multi-tool agent that answers questions about member claims. The target user is an insurance provider. The following two tools are used by this agent:
- A tool for validating the provider ID and NPI number of the provider. This is a simple python function that just returns true for any IDs passed in.
- A tool for returning claims associated with a member. At the moment two members are supported. One member ID is 12345678 (and any date of birth) the second set of claims will be returned for any member ID.

The tools for this demo are accessed via Open API scripts. The python code for the demo is included and can be run as simple Code Engine Functions. Note that you will need to modify the Open API script to point at your Code Engine function endpoints.

The agent in this demo does all the following:

1. Collects a Provider ID and NPI number to validate the provider.
2. Collects the member ID and the date of birth for the member who claims are being questioned.
3. Returns the claims in a markdown table.
4. Allows the user to ask open ended questions about the claims.
5. Makes sure all IDs are in the specified format.
6. Avoids answering questions outside of claims.

## Video of Demo
You can find an mp4 of the demo for this agent in the **video** directory.

## Demo setup
This demo assumes you are using the ADK to load all the files. Setup of the ADK and the environment where you plan to run the demo are outside the scope of this document. You can find details on how to setup your Agent environment at this [link](https://developer.watson-orchestrate.ibm.com/environment/initiate_environment).

1. First, you'll need to create two Code Engine functions and copy the code for the two tools into those functions. The source code for the tools can be found in the **functions** firectory.
2. Next you need to activate the environment where you plan to host the agent. Got to this [link](https://developer.watson-orchestrate.ibm.com/environment/initiate_environment#activating-an-environment) for details on how to activiate your environment.
3. Next you need to modify the server URLs in the Open API scripts for the python function tools you setup in step 1 to point at your function URLs. The open API scripts can be found in the **tools** directory.
4. Next you need to import the tools by running the follow commands (make sure you are in the project root directory when you run these commands):
    - orchestrate tools import -k openapi -f tools/provider-auth.openapi.yml
    - orchestrate tools import -k openapi -f tools/member-profile-server.openapi.yml
5. Next you need to import the agent by running the following command:
    - orchestrate agents import -f claims_voice_agent.yaml

You're now ready to run the agent. 