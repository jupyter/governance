# Bootstrapping Decision Making Bodies

As the new Jupyter governance model is approved and implemented, Jupyter Subprojects will have to establish a formal decision making body. There are a number of challenges associated with this:

- We are moving from an informal model where most Subprojects do not have a formal decision making body, to the formal one described in the Decision Making Guidelines.
- Most Subprojects do not have a well defined decision making body today.
- In the new model, there is flexibility about the size of the formal decision making bodies. Each Subproject will need to also determine how large its formal decision making body is.
- There is a wide range of sizes of Subprojects &mdash; some have a few contributors and others have many dozens.
- We are proposing to establish new Subprojects for certain areas of Project Jupyter, that don’t have an existing history of informal governance.
- The new governance model and [decision making guide](decision_making.md) is designed to support large, highly participatory decision making bodies. As such, even Subprojects that have a clear decision making body today, may wish to increase the size of that body to include more contributors.
- Our current governance model (informal consensus by an informal group lacking clear boundaries) does not have an established mechanism for decisions like this. We believe it will be very difficult for Subprojects to elect a formal governing body and pick its size using informal consensus.
- We wish to avoid each Subproject having layers of meta consensus or voting to establish a process for electing their decision making body.
- We need to take existing Steering Council members into account. There may be Steering Council members that would like to be on the formal decision making body for a Subproject, even though they have not been active on the Suproject for a period of time.

## Proposed framework

We would like to propose the following framework for Subprojects to establish and bootstrap their formal decision making bodies. This framework is not being presented as a set of strict rules, but more as a set of flexible principles that Subprojects can use for this task. The Governance Working Group will be available to meet with all Subprojects to openly discuss how the Subproject can best use and adapt these ideas to their case.

The overall principle of this framework is that of gradual accumulation of the decision making body, rather than bulk election. The process we propose can be briefly outlined as follows:


- Each Subproject typically has a core of individuals who have a long history with the Subproject and have made significant contributions to the Subproject (in many cases, they founded the Subproject). There is universal agreement that these people should be on the formal decision making body for the Subproject. An example would be Min for JupyterHub. This initial group can be as small as a single person and keeping it as small as possible ensures this step will be simple. Let’s call the size of this initial group `N0`.
- Once the initial group or person is established, that group will use the new Decision Making Guidelines to elect the next single member they would like to add to the formal decision making body. At this point, the decision making body would have size `N0+1`.
- At this point, the `N0+1` people would use the Decision Making Guidelines to elect the next single member to add to the decision make body.
- This process continues in an inductive manner where at each point, the current `N` people on the decision making body elect the `N+1` person, or choose to stop electing new members.

This framework has the following characteristics:

- By gradually increasing the size of the decision making body one person at a time, the power implicit in this election process is gradually distributed over a larger group of people.
- At each stage where the new decision making body is considering adding a new person, they can also choose to stop electing additional members. This allows the group to decide on the overall size in an organic, gradual manner.
