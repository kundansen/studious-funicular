# Agentic and Multi-Agentic AI

### Founded on Agent and Multi-Agent Systems (MAS)


## Introduction

Agentic AI is not a new concept! In this article, we will first explore the origins of the term “agentic” and its adoption into the field of AI. Next, we will examine foundational research contributions to Agent and Multi-Agent Systems, which have significantly influenced the development of Agentic Computing (also known as Agentic and Multi-Agentic AI). To better understand the role and potential of Agentic Technology in building modern AI systems, we will analyse the parallels and differences between workflow engines and orchestration engines. Finally, we will discuss how integrating Agentic Technology into an orchestration engine can make it more intelligent, adaptive, and resilient, enhancing its ability to manage complex workflows in dynamic, distributed environments.

## Earliest use of the term “Agentic”

The term “agentic” originates from social and psychological sciences, particularly from the work of Albert Bandura, a renowned psychologist. Bandura introduced the concept of “agentic perspective” in his Social Cognitive Theory during the 1980s.
Albert Bandura’s 1986 book, Social Foundations of Thought and Action: A Social Cognitive Theory, represents one of the earliest formal references to the term “agentic.” In this context, “agentic” refers to the capacity of individuals to act intentionally, make choices, and exert control over their environment and circumstances, highlighting the proactive and deliberate nature of human agency. In Social Cognitive Theory, Albert Bandura introduced the agentic perspective, emphasising that humans are not passive beings shaped solely by environmental forces or internal drives. Instead, they are active agents of their own actions. The concept of “agentic” highlights the human capacity to self-regulate behavior, set and pursue goals, reflect on experiences to inform decision-making, and proactively shape their environment rather than merely responding to it.
Since its initial introduction in psychology, the term “agentic” has been adopted across various disciplines to describe intentionality and autonomy. In sociology, it refers to individuals’ capacity to influence and reshape social structures. In artificial intelligence, “agentic” describes systems or agents with autonomy, intentionality, and the ability to make decisions independently, showcasing its versatility in different fields.
While the term’s roots lie in human behavior and psychology, its modern adoption in AI (ie., Agent and Multi-Agent Systems) and other fields reflects its versatility in describing autonomy and purposeful action.

## Foundational Work on Agent and Multi-Agent Systems

Agent and Multi-Agent Systems (MAS) research significantly influences Agentic Computing (aka Agentic and Multi-Agentic AI), a paradigm focusing on creating autonomous, interactive, and intelligent computational systems. Agentic Computing leverages the foundational principles and advances of agent-based systems to enable self-driven, cooperative, and adaptable computational environments. The field of Agent and Multi-Agent Systems (MAS) has been shaped by numerous pioneering researchers whose foundational work has significantly advanced the domain. Here are some of the key foundational contributors:
1. Michael Wooldridge — A leading figure in the theoretical foundations of agent-based systems, focusing on formal models of multi-agent interactions and agent-oriented software engineering (Wooldridge & Jennings, 1995), (Wooldridge, 2002).
2. Katia Sycara — Renowned for work on coordination, negotiation, and collaboration in MAS, with significant contributions to semantic web technologies and agent-based systems in complex environments (Sycara, 1998), (Sycara & Zeng, 1996).
3. Yoav Shoham — Pioneer in the integration of game theory with MAS, developing frameworks for logical reasoning and agent behavior in strategic settings (Shoham, 1993), (Shoham & Leyton-Brown, 2008).
4. Nicholas R. Jennings — Known for practical and theoretical contributions to autonomous systems and agent-based computing, focusing on distributed artificial intelligence and real-world applications (Jennings & Wooldridge, 1998), (Jennings, 2000).
5. Victor Lesser — One of the earliest contributors to distributed problem-solving and multi-agent coordination, introducing key concepts in cooperative distributed AI and agent architecture (Lesser, 1999), (Decker & Lesser, 1995).
6. Jeffrey S. Rosenschein — Pioneered the use of game theory in MAS, investigating negotiation and automated reasoning in multi-agent environments (Rosenschein & Zlotkin, 1994), (Rosenschein & Genesereth, 1985).
7. Pattie Maes — Known for work on intelligent agents and human-computer interaction, developing early frameworks for autonomous and adaptive agents (Maes, 1994), (Maes, 1995).
8. Sandip Sen — Focused on learning in MAS and adaptive agent behavior, studying mechanisms for agent collaboration and the development of trust in agent systems (Sen & Weiss, 1999), (Sen & Dutta, 2002).
9. Barbara Grosz — Pioneer in collaborative planning and human-agent interaction (Grosz & Kraus, 1996) with specific focus on modelling shared intentions and multi-agent teamwork (Grosz & Kraus, 1999).
10. Gerhard Weiss — Made significant contributions to the development of theoretical foundations, frameworks, and applications of MAS covering topics such as agent communication, coordination, negotiation, learning, and reasoning (Weiss, 1999, 2013).
Agent and Multi-Agent Systems is a very active research and development area in AI. Several key reference sites for the latest research outcome are:
The International Foundation for Autonomous Agents and Multiagent Systems (IFAAMAS) https://tinyurl.com/mrcd3dba
**The Journal Autonomous Agents and Multi-Agent Systems https:**//tinyurl.com/yz87frc7
**The AAMAS Conference Series https:**//aamas2025.org/

## Key Features of Agent Systems

Agent systems, a core component of artificial intelligence, are designed to simulate intelligent behavior by leveraging the following key features:
1. Autonomy — Agents operate independently, making decisions and taking actions without direct human intervention. This independence allows them to perform tasks and adapt to their environment in real-time.
2. Proactiveness — Agents do not merely react to changes in their environment; they are goal-oriented and capable of initiating actions to achieve objectives. They can anticipate needs or potential problems and act to address them.
3. Reactivity — Agents are responsive to changes in their environment, processing input from sensors or data streams and adapting their behavior accordingly. This feature ensures dynamic and context-aware operation.
4. Social Ability — Agents can communicate and collaborate with other agents or systems. This interaction allows them to share information, negotiate, and work together to achieve complex goals, often in multi-agent systems.
5. Learning and Adaptability — Agents can learn from their experiences and adapt their behavior to improve performance over time. This may involve techniques like machine learning, reinforcement learning, or heuristic-based adjustments.
6. Mobility (Optional) — Some agents, known as mobile agents, can move across different systems or networks to perform tasks. This mobility enhances their flexibility and scalability in distributed environments.
7. Goal-Oriented Behavior — Agents are designed with specific goals or objectives in mind. Their actions are directed toward achieving these goals efficiently, often by optimising resources or balancing constraints.
8. Rationality — Agents exhibit rational behavior by selecting actions that maximise their utility or align with predefined objectives. This rationality ensures logical and effective decision-making.
9. Context Awareness — Agents are aware of their operational context, including environmental conditions, available resources, and potential constraints. This awareness enables better decision-making and problem-solving.
10. Scalability — Agents can operate individually or as part of a larger system, making them highly scalable. In multi-agent systems, agents work together in a distributed manner, making the system more robust and capable of handling complex tasks.
11. Flexibility — Agents are designed to adapt to diverse tasks, environments, or changing objectives. This flexibility makes them suitable for a wide range of applications, from automation to dynamic problem-solving.
Agent systems’ ability to combine autonomy, social interaction, and learning makes them essential in advancing intelligent and adaptive technologies. How many of these features are implemented in your Agentic AI System?

## Key Features of Multi-Agent Systems

Multi-Agent Systems (MAS) are composed of multiple interacting agents that collaborate or compete to achieve individual or shared goals. The key features that define MAS are as follows:
1. Distributed and Decentralized Control — In MAS, there is no single point of control. Each agent operates autonomously and makes decisions independently. The decentralised nature enhances system robustness and scalability, as the failure of one agent does not necessarily affect the entire system.
2. Autonomy — Each agent in a MAS can operate without direct intervention from other agents or a central authority. Agents are self-governing and capable of pursuing their individual objectives while interacting with others.
3. Interaction and Communication — Agents in MAS communicate with one another to exchange information, negotiate, or coordinate actions. Communication can occur via predefined protocols (e.g., agent communication languages like FIPA ACL) to ensure interoperability.
4. Cooperation and Coordination — Agents may work together to achieve shared goals, particularly in cooperative MAS. Coordination mechanisms ensure that agents’ actions are aligned and efficient, avoiding conflicts or redundancy.
5. Competition — In some MAS scenarios, agents may compete for resources or goals. Competitive behavior is often modeled using game theory to analyze and predict outcomes.
6. Scalability — MAS can handle a large number of agents, making them suitable for complex and distributed environments. The system can scale by adding or removing agents without significant impact on overall performance.
7. Adaptability — Agents and the MAS as a whole can adapt to dynamic environments, such as changing goals, resource availability, or unexpected events. Agents may learn from their interactions and adjust their strategies accordingly.
8. Heterogeneity — MAS often consist of heterogeneous agents with different capabilities, goals, or roles. This diversity allows the system to tackle complex problems requiring specialised knowledge or functionality.
9. Goal Orientation — Each agent in a MAS typically has its own set of goals or objectives. These goals may align with or conflict with the goals of other agents, requiring negotiation or prioritisation.
10. Emergent Behavior — MAS often exhibit emergent behavior, where the interactions among agents lead to system-wide patterns or outcomes that are not explicitly programmed. This feature makes MAS effective in solving complex, real-world problems.
11. Robustness and Fault Tolerance — The distributed nature of MAS makes them inherently robust, as the system can continue to function even if some agents fail. Fault tolerance is especially valuable in critical applications like robotics or disaster response.
12. Parallelism — Since each agent operates independently, MAS inherently support parallelism. Tasks can be distributed across agents, improving efficiency and reducing computation time.
The combination of autonomy, interaction, and distributed intelligence makes MAS a powerful approach to solving complex, distributed problems in diverse domains. How many of these features are implemented in your Multi-Agentic AI System?
Before we can appreciated how Agentic-AI and Multi-Agentic-AI technologies can significantly contribute to the development of modern AI Systems, let us first look at the parallels and differences between Workflow Engine and Orchestration Engine.

## Workflow Engine vs Orchestration Engine

A workflow engine is a software system that manages, executes, and monitors a sequence of predefined tasks or processes based on a set of rules or logic. It automates workflows within a specific domain or application, coordinating tasks, handling conditional branching, and enabling parallel execution where necessary. Workflow engines are commonly used in business process management (BPM) to streamline operations like approvals, task assignments, or document processing. They provide visibility into workflows, ensure task completion in the correct order, and help optimise efficiency by reducing manual intervention.
An orchestration engine is a software system that automates, coordinates, and manages workflows and processes across multiple systems, services, or applications. It focuses on integrating diverse components into cohesive workflows, ensuring tasks are executed in the correct sequence, managing dependencies, and handling errors or retries. Orchestration engines are commonly used in distributed environments, such as managing microservices, cloud infrastructures, or CI/CD pipelines. They enable scalability, adaptability, and efficient resource utilisation by automating complex, multi-system interactions and providing centralised control and monitoring of the entire process.
The parallelism between a workflow engine and an orchestration engine lies in their shared ability to coordinate and manage a series of tasks, processes, or services to achieve a specific goal. Both systems provide mechanisms to define, execute, and monitor complex sequences of operations. However, they differ in scope, focus, and implementation as depicted in the following table:
Press enter or click to view image in full size

**Table-1:** Workflow Engine vs Orchestration Engine

## Enriching Orchestration Engine with Agentic (Multi-Agentic) Technology

Building today’s AI systems that involves multiple API calls, calling external microservices, calling services across the cloud infrastructure, almost always will require an Orchestration Engine. Enriching an orchestration engine with agentic technology involves embedding features that empower the system to act autonomously, adapt dynamically, and make intelligent decisions while coordinating complex workflows. Here’s how you can achieve this:

### 1. Introduce Autonomous Decision-Making

**Dynamic Task Assignment:** Use agentic capabilities to dynamically allocate tasks based on real-time analysis of system states, resource availability, or priority levels.
**Context-Aware Execution:** Enable the engine to analyse context and make decisions, such as selecting optimal paths for task execution or adapting workflows to unexpected changes.

### 2. Incorporate Learning and Adaptability

**Reinforcement Learning:** Implement machine learning models that allow the engine to learn from past workflows and improve efficiency or error-handling over time.
**Adaptive Scheduling:** Equip the engine to adjust task priorities or sequences based on performance metrics, bottlenecks, or system demands.

### 3. Enable Proactive Behavior

**Anomaly Detection and Recovery:** Use predictive analytics to identify potential failures or inefficiencies and proactively reroute workflows or trigger corrective actions.
**Goal-Oriented Processes:** Allow the engine to evaluate high-level objectives and autonomously determine the best strategies to achieve them.

### 4. Enhance Communication and Collaboration

**Multi-Agent Coordination:** Integrate agent-based components that collaborate within the orchestration system to optimise distributed tasks or handle interdependencies.
**Agent-to-Agent Communication:** Implement protocols for agents within the system to negotiate, share knowledge, and resolve conflicts during workflow execution.

### 5. Embed Rule-Based Reasoning

Use symbolic AI or rule-based systems to complement data-driven approaches, enabling the engine to reason logically about constraints, dependencies, and conditions within workflows.

### 6. Focus on Explainability

**Transparent Decision-Making:** Equip the system with mechanisms to explain its actions and decisions, improving trust and aiding in debugging or optimisation efforts.

### 7. Integrate with Knowledge Graphs and Ontologies

**Contextual Awareness:** Use knowledge graphs to provide semantic understanding of tasks, relationships, and workflows, enabling more intelligent decision-making.
**Resource Optimisation:** Leverage ontologies to model domain-specific rules and optimise resource allocation.

### 8. Add Distributed Intelligence

**Agentic Subsystems:** Break down the orchestration engine into smaller, agentic subsystems capable of handling localised tasks autonomously while aligning with the overall orchestration objectives.
By integrating agentic technology, an orchestration engine becomes more intelligent, adaptive, and resilient, enhancing its ability to manage complex workflows in dynamic, distributed environments.

## Conclusion

Agentic AI, though not a new concept, has its roots in social and psychological sciences before being adopted into the field of AI. Key foundational research contributions to Agent and Multi-Agent Systems have played a significant role in advancing Agentic AI. To understand how Agentic Technology contributes to modern AI systems, we explored the parallels and differences between workflow engines and orchestration engines. Both share the ability to coordinate and manage tasks, processes, or services to achieve specific goals, but they differ in scope, focus, and implementation. Building modern AI systems often involves coordinating multiple API calls, interacting with microservices, and accessing services across cloud infrastructures, making an orchestration engine an essential component. By integrating Agentic Technology, orchestration engines can be enhanced with greater intelligence, adaptability, and resilience, enabling them to efficiently manage complex workflows in dynamic and distributed environments.

## References

Decker, K., & Lesser, V. (1995). “Designing a family of coordination algorithms.” In Proceedings of the First International Conference on Multi-Agent Systems (pp. 73–80).
Gerhard Weiss (1999). “Multiagent Systems: A Modern Approach to Distributed Artificial Intelligence” (1999, 2nd edition in 2013), The MIT Press.
Grosz, B. J., & Kraus, S. (1996). “Collaborative plans for complex group action.” Artificial Intelligence, 86(2), 269–357.
Grosz, B. J., & Kraus, S. (1999). “The evolution of SharedPlans.” In Foundations of Rational Agency (pp. 227–262). Springer.
Jennings, N. R. (2000). “On agent-based software engineering.” Artificial Intelligence, 117(2), 277–296.
Jennings, N. R., & Wooldridge, M. (1998). “Applications of intelligent agents.” In Agent Technology (pp. 3–28). Springer.
Lesser, V. R. (1999). “Cooperative multiagent systems: A personal view of the state of the art.” IEEE Transactions on Knowledge and Data Engineering, 11(1), 133–142.
Maes, P. (1994). “Agents that reduce work and information overload.” Communications of the ACM, 37(7), 30–40.
Maes, P. (1995). “Artificial life meets entertainment: Lifelike autonomous agents.” Communications of the ACM, 38(11), 108–114.
Rosenschein, J. S., & Zlotkin, G. (1994). “Rules of Encounter: Designing Conventions for Automated Negotiation among Computers.” MIT Press.
Rosenschein, J. S., & Genesereth, M. R. (1985). “Deals among rational agents.” In Proceedings of the Ninth International Joint Conference on Artificial Intelligence (pp. 91–99).
Sen, S., & Weiss, G. (1999). “Learning in multiagent systems.” In Multiagent Systems (pp. 259–298). MIT Press.
Sen, S., & Dutta, P. S. (2002). “The evolution and stability of cooperative traits.” In Proceedings of the First International Joint Conference on Autonomous Agents and Multiagent Systems: Part 3 (pp. 1114–1120).
Shoham, Y. (1993). “Agent-oriented programming.” Artificial Intelligence, 60(1), 51–92.
Shoham, Y., & Leyton-Brown, K. (2008). “Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations.” Cambridge University Press.
Sycara, K. (1998). “Multiagent systems.” AI Magazine, 19(2), 79–92.
Sycara, K., & Zeng, D. (1996). “Coordination of multiple intelligent software agents.” International Journal of Cooperative Information Systems, 5(02n03), 181–211.
Wooldridge, M., & Jennings, N. R. (1995). “Intelligent agents: Theory and practice.” The Knowledge Engineering Review, 10(2), 115–152.
Wooldridge, M. (2002). “An Introduction to Multi-Agent Systems.” John Wiley & Sons.
