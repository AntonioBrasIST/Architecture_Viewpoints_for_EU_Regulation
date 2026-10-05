# Architecture_Viewpoints_for_EU_Regulation
Repository for the thesis: Stakeholder-Specific Architecture Viewpoints for EU Regulation: A Generative AI-Supported Method

# Abstract

European Union regulation imposes organizational obligations whose implications for individual stakeholders are often difficult to identify. Translating these obligations into representations of daily activities, responsibilities, and dependencies requires a systematic connection between legal requirements and operational evidence. This dissertation proposes a human-supervised method, supported by GenAI, for identifying, specifying, and materializing stakeholder-specific architecture viewpoints.

Following Design Science Research Methodology and grounded in ISO/IEC/IEEE 42010, the method combines stakeholder interviews, operational-footprint extraction, regulatory relevance analysis, viewpoint specification, and ArchiMate model generation. Traceability links architectural elements and relationships to binding legal text and documented operational evidence, while explicit ownership distinctions, human approval gates, and cross-artifact reconciliation constrain generated content.

The method is demonstrated using the DORA through the perspectives of impacted stakeholders. The resulting Architecture Descriptions relate regulatory requirements to role-specific work while distinguishing direct responsibilities, external dependencies, and uncertain ownership. Preliminary stakeholder feedback indicates that the formal views can support regulatory understanding and reveal missing operational context, enabling viewpoint refinement. It also identifies limitations in explanatory narratives and simplified diagrams. The demonstrations support the feasibility of the approach, with opportunities for further development. The contribution is a traceable process for communicating stakeholder-specific regulatory impact without assessing organizational compliance.

## Repository folders

- `Dissertation/`  
  Contains the LaTeX source, bibliography, images, and supporting material for the MSc dissertation, as well as the thesis PDF and extended summary. 

- `GenAI_Tools/`  
  Contains a historical snapshot of agent and skill definitions. It is retained for reference. These should be copied into the skills and agents folder of the coding agent of your choice.

- `Methodology/`  
  Contains the human-supervised methodology pipeline, stakeholder case artefacts, validation tools, and tests used to develop regulation-aware ArchiMate viewpoints.

- `TraceabilityMatrixCreator/`  
  Contains the .NET application that converts bundled EUR-Lex legal documents into structured Excel traceability matrices, used by the methodology to anchor requirements to legal text.

## Repository utility and execution

The repository is already prepared with the necessary files to execute the methodology, as well as the necessary files for agent context (AGENTS.md)
  
