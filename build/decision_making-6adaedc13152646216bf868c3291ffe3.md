# Decision-Making Guide

This document describes how Jupyter’s governing bodies (generally called "councils") make decisions. Because individuals often work across multiple decision-making groups, all Jupyter governing bodies are expected to follow this approach.

We seek to honor the principles of collaboration, inclusive participation, and responsive decision making. Some aspects of this decision-making guide are required of all teams. Others are provided as recommendations and are optional. We have clearly noted the optional aspects of decision making below.

Finally, the [Jupyter Executive Council](executive_council.md) may either intervene, or be called upon by members of a team, in the event that issues arise in the decision-making process. This includes, but is not limited to: process ambiguity, violations of the decision-making process, mitigating circumstances that require process exceptions, etc.

## Required aspects of decision making

The decision-making process is intended to balance broad participation of stakeholders with agility. While the size of decision-making bodies may vary (e.g., software projects can range from a handful to dozens of decision makers), all need to find this balance. The guidelines below cannot fully capture the role of human judgment and discretion.

All official Jupyter projects, working groups, governing bodies, and official initiatives must have a clearly-defined and documented council. Formally, these councils make decisions using consensus seeking with an option to call a vote to move the decision forward. All decisions, whether made by informal consensus or by formal vote, may be revisited; however, if a council finds itself frequently revisting consensus-based decisions, this should be viewed as an indication that the council's understanding of informal consensus may need to be reviewed.

Depending on the council, decisions may be proposed by members of the council or by a broader group of stakeholders/contributors.

**Informal consensus seeking.** Decision making starts with informal consensus seeking through discussion. The goal of this phase is to refine the proposal, consider alternatives, weigh trade-offs, and attempt to find informal consensus. The legitimacy of the consensus-seeking process is predicated on all stakeholders having their voices heard, so councils must be proactive in providing opportunities for all relevant stakeholders to provide input. If the council arrives at informal consensus, they may immediately move to document and enact the decision. This is the consensus-seeking phase.

**Calling a vote.** When the discussion matures during the consensus-seeking phase, any member of the council can call the matter to a vote. When that member (the sponsor) calls the vote, they shall summarize the proposal in its current form for the entire council. After the proposal is seconded by another member of the council, members have seven days to vote. The council may consider longer voting periods as necessary for special circumstances, or _shorter periods only if all voting members are present_. The decision will be determined by a simple majority of non-blank votes for binary decisions (i.e., approving a proposal) and ranked choice for multi-class decisions (one among many, or several among many). The sponsor may update the proposal at any point during the voting period, in which case the voting period will be reset.

**Voter participation and quorum.** All members of a council are required to participate in at least 2/3 of formal votes of that council per calendar year (councils can decide how to account for the specifics of this in low-activity projects, etc.). Members that have not met the 2/3 vote participation threshold for a year will automatically be asked to step down at the end of that year. Those individuals remain eligible to rejoin the council in the future as they become available to participate at the required level. The quorum for all formal votes will be 50% and a "blank" option will always be included, with the "blank" option counting towards the quorum but not included in totals for calculating results. The participation and quorum figures in this guide should be considered a minimum standard, individual councils may decide to adopt more stringent rules if appropriate.

**Recording.** Once a decision has been made during the consensus-seeking phase or by a formal vote, the council will record the decision, e.g., in Team Compass issues for councils whose workflow is on GitHub or other equivalent and publicly visible mechanisms. 

## Optional aspects of decision making

While the previous section is prescriptive for all Jupyter councils, the following are recommended guidelines rather than mandatory procedures.

- Councils should not call a vote to short-circuit an ongoing discussion that is still productive in terms of exploring ideas and feedback. Votes should be called only when discussion has explored the space and stakeholders have provided input.
- Councils should proactively solicit input from relevant stakeholders and should not assume that silence is consent without attempting to reach out to those individuals.
- If you are interested in a decision being made, it is your responsibility to encourage voting member/stakeholder/community participation in the decision-making process. If you cannot get such participation, you may want to hold off on doing any significant work on the matter.
- Special guidelines for software projects making decisions:
  - Add a link to this document in your issue and PR templates along with a link to the council membership (see recommended language below).
  - Create `seeking consensus`, `vote`, and `decision made` issue labels to make it easy to find issues/PRs where decisions are discussed and resolved.
  - When a vote is called on GitHub, the sponsor should summarize the decision and paste a checklist of the voting members to use in voting in the top entry (description) of the issue/PR.
  - When communications (in whatever number of channels) point to a discussion that requires a project-wide decision, and before major implementation work starts, a standalone issue should be opened that summarizes the issue, points to relevant prior discussions, and calls for an explicit vote/decision. This issue should be tightly scoped to the relevant decision only, and include the `vote` label.
  - When an implementation of a decision appears in a pull request, link to the relevant `vote` issue.
- Councils and those proposing decisions should explicitly distinguish between decisions that are two-way doors (easy to reverse later) and one-way doors (difficult or impossible to reverse later). For one-way doors, councils should carefully weigh alternatives and tradeoffs and take extra care to ensure broad participation and stakeholder input. For two-way doors, councils should feel free to move quickly, without compromising the principles and procedures described herein.

## Language for issue/PR template

Project Jupyter councils make decisions using a consensus-seeking model. You can read about this model here (link). The council for this project is documented here (link).
