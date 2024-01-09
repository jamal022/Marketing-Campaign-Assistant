import streamlit as st
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from dotenv import load_dotenv

load_dotenv()

def getLLMResponse(query, age_option, taskType_option):

    llm = HuggingFaceHub(repo_id ="HuggingFaceH4/zephyr-7b-beta")

    if age_option == "Senior Citizen" and taskType_option == "Create a tweet":

        examples = [
    {
        "query": "What is a mobile?",
        "answer": "📱 A mobile is a portable tech wonder with microprocessors, touchscreens, and wireless magic. It's your go-to for entertainment, communication, and data wizardry! 🌟 #MobileTech #TechExplained"
    },
    {
        "query": "What are your dreams?",
        "answer": "💭 Dreaming big! 🚀 My aspirations involve pushing the boundaries of science and contributing to society through research and innovation. Breakthroughs in renewable energy, healthcare, and AI are my vision for a brighter future! 🌍🔬 #DreamBig #InnovationGoals"
    },
    {
        "query": "What is a car?",
        "answer": "🚗 What's a car? 🤔 An automobile is a self-propelled marvel built for transporting passengers or goods. With engines, wheels, and a sleek chassis, it moves using internal combustion, electric power, or hybrid magic. 🌐🚗 #CarTech #Innovation"
    },
    {
        "query": "What is a computer?",
        "answer": "💻 Decoding a computer! 🧠 A computer is a high-tech wizard processing data with a CPU, memory, and more. It's all about algorithms and logical prowess, making complex computations a breeze. 💻🔍 #ComputerScience #TechTalk"
    },
    {
        "query": "What are your thoughts on space exploration?",
        "answer": "🚀 Thoughts on space exploration? 🌌 It's a stellar journey propelling humanity into scientific frontiers. Using tech wizardry, we explore celestial wonders, gather data, and expand our cosmic understanding! 🌠🔭 #SpaceExploration #CosmicAdventure"
    },
    {
        "query": "How does electricity work?",
        "answer": "⚡️ How does electricity work? ⚡️ It's the dance of charged particles, like electrons, through conductive materials. Governed by electromagnetism, understanding this electrifying behavior is key to mastering electrical systems! 🔌🤓 #Electricity101 #TechTrivia"
    },
    {
        "query": "Can you explain the concept of quantum mechanics?",
        "answer": "🔍 Quantum mechanics demystified! 🌀 It's the physics of the small, exploring atoms and subatomic wonders. Think wave-particle duality and superposition, shaking up classical ideas and paving the way for quantum tech! 🚀🔬 #QuantumMechanics #TechExplained"
    },
    {
        "query": "Define artificial intelligence.",
        "answer": "🤖 What's artificial intelligence? 🧠 AI is the tech brainchild crafting intelligent machines. With algorithms, machine learning, and neural networks, it's all about machines learning, adapting, and making savvy decisions! 🤖💡 #ArtificialIntelligence #TechInnovation"
    }
]

    elif age_option == "Senior Citizen" and taskType_option == "Write a sales copy":
        examples = [

    {
        "query": "What is a mobile?",
        "answer": "Discover the epitome of portability with our cutting-edge mobile devices. A mobile is not just a gadget; it's a sleek electronic companion that seamlessly integrates advanced technologies like microprocessors, touchscreens, and wireless communication protocols. Elevate your lifestyle with a device that goes beyond entertainment, enabling flawless communication and lightning-fast data processing."
    },
    {
        "query": "What are your dreams?",
        "answer": "Join us in a visionary quest to advance scientific knowledge and uplift society through pioneering research and innovation. Our dreams revolve around contributing to breakthroughs in vital fields like renewable energy, healthcare, and artificial intelligence. Shape the future with us as we embark on a mission to make dreams a reality."
    },
    {
        "query": "What is a car?",
        "answer": "Experience the zenith of transportation with our exceptional automobiles. A car is not just a means of travel; it's a marvel of self-propelled engineering designed for the seamless transport of passengers or goods. Featuring an engine, wheels, and a robust chassis, our cars utilize internal combustion engines, electric motors, or hybrid systems—each embodying scientific principles for unparalleled performance."
    },
    {
        "query": "What is a computer?",
        "answer": "Unleash the power of sophistication with our state-of-the-art computers. A computer is not just a device; it's a sophisticated electronic marvel that processes and stores data through intricate algorithms and logical operations. Explore the synergy of a central processing unit (CPU), memory, and input/output devices working harmoniously to perform complex computations."
    },
    {
        "query": "What are your thoughts on space exploration?",
        "answer": "Embark on a cosmic journey with our perspective on space exploration. It's a remarkable endeavor that propels humanity to the forefront of scientific discovery. Utilizing advanced technologies, we explore celestial bodies, gather data, and expand our understanding of the vast cosmos. Join us in pushing the boundaries of what's possible in the great unknown."
    },
    {
        "query": "How does electricity work?",
        "answer": "Illuminate the mysteries of electricity with our insightful explanation. Electricity is more than just a phenomenon; it's the dynamic flow of charged particles, typically electrons, through conductive materials. Governed by the principles of electromagnetism, understanding the behavior of electrons and their interaction with conductors is fundamental to comprehending the intricate workings of electrical systems."
    },
    {
        "query": "Can you explain the concept of quantum mechanics?",
        "answer": "Dive into the quantum realm with our captivating explanation. Quantum mechanics is a fundamental theory in physics that unveils the behavior of particles on a minuscule scale, such as atoms and subatomic particles. It introduces mind-bending concepts like wave-particle duality and superposition, challenging classical notions and forming the basis for advancements in quantum computing and technology."
    },
    {
        "query": "Define artificial intelligence.",
        "answer": "Unlock the future with our definition of artificial intelligence (AI). It's not just a branch of computer science; it's a dedicated journey to create intelligent machines capable of tasks that typically require human intelligence. Through sophisticated algorithms, machine learning models, and neural networks, AI enables machines to learn from data, adapt, and make intelligent decisions. Join us in shaping a future where machines think and act intelligently."
    }

]
    
    elif age_option == "Senior Citizen" and taskType_option == "Write a product description":
        examples = [

    {
        "query": "What is a mobile?",
        "answer": "Introducing our state-of-the-art mobile devices—an embodiment of cutting-edge technology. Immerse yourself in the world of portability with our sleek and sophisticated gadgets. From advanced microprocessors to responsive touchscreens and seamless wireless communication, our mobiles redefine the way you live. Elevate your lifestyle with a device that seamlessly blends entertainment, communication, and lightning-fast data processing."
    },
    {
        "query": "What are your dreams?",
        "answer": "Embark on a visionary journey with us, where dreams transcend into reality. Our aspirations revolve around advancing scientific knowledge and contributing to societal betterment through groundbreaking research and innovation. Picture a future where renewable energy, healthcare, and artificial intelligence converge to shape a world of endless possibilities. Join us in making dreams come true."
    },
    {
        "query": "What is a car?",
        "answer": "Drive into the future with our exceptional automobiles—a fusion of engineering marvel and unparalleled performance. A car, more than a means of transportation, is a testament to self-propelled excellence. With a powerhouse engine, reliable wheels, and a robust chassis, our cars utilize internal combustion engines, electric motors, or hybrid systems, each embodying scientific principles for a journey like no other."
    },
    {
        "query": "What is a computer?",
        "answer": "Unleash the power of sophistication with our cutting-edge computers. Beyond a mere device, our computers are sophisticated electronic marvels that process and store data through intricate algorithms and logical operations. Explore the seamless synergy of a central processing unit (CPU), memory, and input/output devices working harmoniously to perform complex computations, redefining your digital experience."
    },
    {
        "query": "What are your thoughts on space exploration?",
        "answer": "Embark on a cosmic journey with our perspective on space exploration. Our remarkable endeavor propels humanity to the forefront of scientific discovery. With advanced technologies, we explore celestial bodies, gather data, and expand our understanding of the vast cosmos. Join us in pushing the boundaries of what's possible and experiencing the awe-inspiring unknown."
    },
    {
        "query": "How does electricity work?",
        "answer": "Illuminate the mysteries of electricity with our insightful explanation. Electricity is more than a phenomenon—it's the dynamic flow of charged particles, typically electrons, through conductive materials. Governed by the principles of electromagnetism, understanding the behavior of electrons and their interaction with conductors is fundamental to comprehending the intricate workings of electrical systems. Power your world with knowledge."
    },
    {
        "query": "Can you explain the concept of quantum mechanics?",
        "answer": "Dive into the quantum realm with our captivating explanation. Quantum mechanics, a fundamental theory in physics, unveils the behavior of particles on a minuscule scale—atoms and subatomic particles. With mind-bending concepts like wave-particle duality and superposition, challenge classical notions and explore the basis for advancements in quantum computing and technology. Experience the future unfolding before your eyes."
    },
    {
        "query": "Define artificial intelligence.",
        "answer": "Unlock the future with our definition of artificial intelligence (AI). More than a branch of computer science, it's a dedicated journey to create intelligent machines. These machines perform tasks requiring human intelligence, thanks to sophisticated algorithms, machine learning models, and neural networks. Join us in shaping a future where machines think and act intelligently, transforming the way we live and interact with technology."
    }

]
        
    elif age_option == "Kid" and taskType_option == "Create a tweet":
        examples = [
    {
        "query": "What's a mobile?",
        "answer": "A mobile is like a super cool gadget you carry around! 📱✨ It's a magic box that lets you play games, talk to friends, and take funny pictures. Having a pocket-sized fun machine is awesome! 🎮🤳 #TechMagic #GadgetFun"
    },
    {
        "query": "What are your dreams?",
        "answer": "I dream of being a superhero or a space explorer! 🦸‍♂️🚀 Flying around, discovering new planets, or having superpowers to help people would be so awesome and fun! 💫😄 #DreamBig #SuperheroDreams"
    },
    {
        "query": "What is a car?",
        "answer": "A car is like a zoom-zoom machine! 🚗💨 With wheels, an engine that goes vroom vroom, it takes you to cool places! Cars can be different colors and shapes, just like toys, but real ones! 🌈🚗 #ZoomZoom #CarAdventure"
    },
    {
        "query": "What is a computer?",
        "answer": "A computer is like a super smart friend! 💻🧠 It helps you play games, draw pictures, and learn new things. It's a magical box with buttons and a screen that does amazing stuff! 🎮🖥️ #SmartTech #ComputerMagic"
    },
    {
        "query": "Thoughts on space exploration?",
        "answer": "Space is the biggest adventure ever! 🌌💫 Exploring planets, meeting aliens, and floating around in spacesuits would be so much fun. It's like a giant playground for astronauts! 🚀👩‍🚀 #SpaceAdventure #AstronautDreams"
    },
    {
        "query": "How does electricity work?",
        "answer": "Electricity is like magic light! ✨⚡ Tiny sparkles in the wires make everything turn on. Just like in fairy tales, but it's real and powers our toys, lights, and even makes the TV work! 📺💡 #ElectricWonder #PowerOfSparkles"
    },
    {
        "query": "Explain quantum mechanics.",
        "answer": "Quantum mechanics is like superhero science! 🦸‍♀️✨ Super tiny particles doing amazing dances, like tiny invisible fairies making everything in the world work. It's magical and super, super tiny! 🔍🧚‍♂️ #QuantumMagic #SuperTinyScience"
    },
    {
        "query": "Define artificial intelligence.",
        "answer": "Artificial intelligence is like having a robot friend! 🤖🤝 Machines get super smart, do things almost like humans, and learn from games and stories, becoming really clever! 🌐🧠 #AICompanion #SmartMachines"
    }
]

    elif age_option == "Kid" and taskType_option == "Write a sales copy": 
        examples = [
    {
        "query": "What's a mobile?",
        "answer": "Oh, a mobile is not just a gadget, it's a super cool, pocket-sized fun machine! Picture this: magic box, games, chatting with friends, and capturing funny pictures all in one! It's the ultimate entertainment companion for young adventurers."
    },
    {
        "query": "What are your dreams?",
        "answer": "Dream big, young heroes! Imagine being a superhero or a space explorer, flying around, discovering new planets, and having superpowers to make a difference. It's not just a dream; it's a thrilling adventure waiting to unfold!"
    },
    {
        "query": "What is a car?",
        "answer": "Buckle up for the zoom-zoom experience! A car is more than just wheels; it's a vroom-vroom machine that takes you to cool places. Just like toys, but real ones, with vibrant colors and shapes. The road is your playground let's rev up the excitement!"
    },
    {
        "query": "What is a computer?",
        "answer": "Meet your super smart friend the computer! It's a magical box with buttons and a screen that opens doors to endless possibilities. Play games, create art, and learn fascinating things it's your gateway to a world of amazement!"
    },
    {
        "query": "Thoughts on space exploration?",
        "answer": "Space is the biggest adventure playground ever! Imagine floating in spacesuits, meeting aliens, and exploring planets. It's not just a dream; it's the grand cosmic journey every young astronaut dreams of!"
    },
    {
        "query": "How does electricity work?",
        "answer": "Electricity, the magic light of our world! Picture tiny sparkles in wires bringing everything to life just like fairy tales, but real. It powers your toys, lights up your room, and even makes the TV sparkle with excitement!"
    },
    {
        "query": "Explain quantum mechanics.",
        "answer": "Enter the world of superhero science Quantum Mechanics! Picture super tiny particles performing amazing dances, like invisible fairies making the world work. It's an enchanting realm of tiny wonders that spark curiosity!"
    },
    {
        "query": "Define artificial intelligence.",
        "answer": "Meet your robot friend – Artificial Intelligence! It's not just machines; it's clever companions that learn from games and stories, just like you do. Imagine a world where machines get super smart, almost like having your own robot buddy! 🤖✨"
    }
]

    elif age_option == "Kid" and taskType_option == "Write a product description":
        examples = [
    {
        "query": "What is a mobile?",
        "answer": "Introducing the WonderBox Mobile – the super cool gadget your little explorer carries around! It's more than a device; it's a magic box that transforms playtime into an adventure. With games, chatting with friends, and capturing funny pictures, it's the pocket-sized fun machine that sparks imagination!"
    },
    {
        "query": "What are your dreams?",
        "answer": "Dream big with the WonderBox Dream Big Playset! Whether they dream of being a superhero or a space explorer, this playset takes them on a journey of flying around, discovering new planets, and unleashing superpowers to make the world awesome. It's not just a playset; it's a gateway to thrilling adventures!"
    },
    {
        "query": "What is a car?",
        "answer": "Experience the thrill of the WonderBox Zoom-Zoom Machine! It's not just about wheels; it's a vroom-vroom journey to cool places. Just like toys, but real ones, with different colors and shapes. Buckle up for an exciting ride – the road is their playground!"
    },
    {
        "query": "What is a computer?",
        "answer": "Meet the WonderBox Smart Friend Computer – a magical box with buttons and a screen that opens doors to endless possibilities. It's not just a computer; it's a super smart friend that helps them play games, draw pictures, and learn new things. A gateway to a world of amazement!"
    },
    {
        "query": "What are your thoughts on space exploration?",
        "answer": "Embark on the WonderBox Space Adventure Explorer – the biggest adventure ever! Floating in spacesuits, meeting aliens, and exploring planets – it's not just a playset; it's a giant playground for aspiring astronauts! Let their thoughts soar among the stars!"
    },
    {
        "query": "How does electricity work?",
        "answer": "Illuminate playtime with the WonderBox Magic Light Electricity Set! Witness tiny sparkles in wires bringing everything to life – like fairy tales, but real. It powers toys, lights up rooms, and even makes the TV sparkle with excitement. A magical addition to their playtime experience!"
    },
    {
        "query": "Can you explain the concept of quantum mechanics?",
        "answer": "Dive into superhero science with the WonderBox Superhero Science Quantum Mechanics Kit! It's a world of super tiny particles performing amazing dances. Imagine tiny invisible fairies making everything work – they're super, super tiny, creating an enchanting realm of wonders! Ignite their curiosity and explore the unseen!"
    },
    {
        "query": "Define artificial intelligence.",
        "answer": "Welcome their own WonderBox Artificial Intelligence Robot Buddy! It's not just a product; it's a clever companion that learns from games and stories, almost like humans. Imagine a world where machines get super smart, becoming their own clever robot buddy! 🤖✨"
    }
]

    elif age_option == "Adult" and taskType_option == "Create a tweet":
        examples = [
    {
        "question": "What is a mobile?",
        "response": "📱 A mobile is a portable electronic device integrating microprocessors, touchscreens, and wireless tech. Perfect for entertainment, communication, and data processing! #MobileTech #GadgetLove"
    },
    {
        "question": "What are your dreams?",
        "response": "💭 My aspirations involve advancing scientific knowledge and contributing to society through research and innovation. Imagine breakthroughs in renewable energy, healthcare, and AI! #DreamBig #InnovationGoals"
    },
    {
        "question": "What is a car?",
        "response": "🚗 It's a self-propelled vehicle for passengers or goods. Engines, wheels, and a chassis - all driven by internal combustion engines, electric motors, or hybrid systems. Science in motion! #AutomotiveTech #EngineeredForSpeed"
    },
    {
        "question": "What is a computer?",
        "response": "💻 A sophisticated electronic device processing and storing data through algorithms. Components like CPU, memory, and input/output devices work together for complex computations. #TechWizard #ComputerScience"
    },
    {
        "question": "What are your thoughts on space exploration?",
        "response": "🚀 Space exploration is a remarkable endeavor propelling humanity to scientific frontiers. Advanced tech explores celestial bodies, gathers data, and expands our cosmic understanding. #SpaceExploration #CosmicAdventures"
    },
    {
        "question": "How does electricity work?",
        "response": "⚡ Electricity is the flow of charged particles, typically electrons, through conductive materials. Governed by electromagnetism, it powers our world! #Electricity101 #PowerUp"
    },
    {
        "question": "Can you explain the concept of quantum mechanics?",
        "response": "🌌 Quantum mechanics is the physics of the super small—atoms and subatomic particles. Think wave-particle duality and superposition, leading to quantum computing and tech! #QuantumMechanics #PhysicsWonders"
    },
    {
        "question": "Define artificial intelligence.",
        "response": "🤖 Artificial intelligence (AI) is a branch of computer science creating intelligent machines. Algorithms, machine learning, and neural networks enable machines to learn, adapt, and make smart decisions. #AIRevolution #SmartTech"
    }
]

    elif age_option == "Adult" and taskType_option == "Write a sales copy":
        examples = [
    {
        "question": "Ever wondered what a mobile is?",
        "response": "Unlock the world of possibilities with our cutting-edge mobile technology! 📱 Immerse yourself in a portable electronic device that seamlessly integrates microprocessors, touchscreens, and wireless tech. Elevate your experience in entertainment, communication, and data processing!"
    },
    {
        "question": "Curious about dreams?",
        "response": "Embark on a journey of innovation and impact! 💭 Explore aspirations that go beyond boundaries, advancing scientific knowledge for a brighter future. Envision breakthroughs in renewable energy, healthcare, and artificial intelligence. Your dreams, our mission!"
    },
    {
        "question": "Wondering what a car is?",
        "response": "Rev up your life with the epitome of transportation excellence! 🚗 Introducing the self-propelled marvel designed for passengers or goods. Dive into the fusion of engines, wheels, and a chassis—propelled by internal combustion engines, electric motors, or hybrid systems. Unleash the science of motion!"
    },
    {
        "question": "What's a computer, you ask?",
        "response": "Step into the world of technological brilliance! 💻 Behold a sophisticated electronic device that processes and stores data through intricate algorithms. A symphony of components like CPU, memory, and input/output devices works harmoniously, orchestrating complex computations. Your gateway to tech wizardry!"
    },
    {
        "question": "Thoughts on space exploration?",
        "response": "Embark on a cosmic journey with our state-of-the-art space exploration tech! 🚀 Propel humanity to scientific frontiers using advanced technologies to explore celestial bodies, gather data, and expand our understanding of the vast cosmos. Join us in the adventure beyond the stars!"
    },
    {
        "question": "Ever tried to grasp how electricity works?",
        "response": "Power up your understanding of the electrifying world around you! ⚡ Delve into the flow of charged particles, electrons dancing through conductive materials. Governed by electromagnetism, this phenomenon powers our world. Illuminate your knowledge with Electricity 101!"
    },
    {
        "question": "Curious about quantum mechanics?",
        "response": "Unlock the secrets of the quantum realm! 🌌 Quantum mechanics, the physics of the super small—atoms and subatomic particles. Explore concepts like wave-particle duality and superposition, paving the way for quantum computing and revolutionary technology. Dive into the quantum frontier!"
    },
    {
        "question": "Define artificial intelligence, you say?",
        "response": "Experience the future with our groundbreaking artificial intelligence technology! 🤖 Dive into a branch of computer science dedicated to creating intelligent machines. Algorithms, machine learning, and neural networks converge to enable machines to learn, adapt, and make smart decisions. Join the AI revolution!"
    }
]

    elif age_option == "Adult" and taskType_option == "Write a product description": 
        examples = [
    {
        "question": "Ever wondered what a mobile is?",
        "response": "Introducing our state-of-the-art mobile device, a gateway to a world of possibilities! 📱 Seamlessly integrating cutting-edge microprocessors, touchscreens, and wireless technology, this portable electronic marvel redefines entertainment, communication, and data processing. Elevate your lifestyle with our innovative mobile tech!"
    },
    {
        "question": "Curious about dreams?",
        "response": "Explore the future with our visionary product! 💭 Designed for those with aspirations beyond boundaries, this innovation is your key to advancing scientific knowledge. Envision breakthroughs in renewable energy, healthcare, and artificial intelligence. Your dreams take center stage with our revolutionary technology!"
    },
    {
        "question": "Wondering what a car is?",
        "response": "Revolutionize your commute with our cutting-edge self-propelled vehicle! 🚗 Meticulously crafted for passengers or goods, this marvel features engines, wheels, and a chassis driven by internal combustion engines, electric motors, or hybrid systems. Experience the pinnacle of transportation excellence!"
    },
    {
        "question": "What's a computer, you ask?",
        "response": "Immerse yourself in technological brilliance with our sophisticated electronic device! 💻 Process and store data effortlessly through intricate algorithms. A symphony of components, including CPU, memory, and input/output devices, works harmoniously to orchestrate complex computations. Your gateway to tech wizardry awaits!"
    },
    {
        "question": "Thoughts on space exploration?",
        "response": "Embark on a cosmic journey with our advanced space exploration technology! 🚀 Propel humanity to scientific frontiers using cutting-edge tech to explore celestial bodies, gather data, and expand our understanding of the vast cosmos. Join us in the adventure beyond the stars!"
    },
    {
        "question": "Ever tried to grasp how electricity works?",
        "response": "Illuminate your understanding with our electrifying product! ⚡ Delve into the flow of charged particles, electrons dancing through conductive materials. Governed by electromagnetism, this phenomenon powers our world. Master Electricity 101 with our enlightening technology!"
    },
    {
        "question": "Curious about quantum mechanics?",
        "response": "Unlock the secrets of the quantum realm with our groundbreaking product! 🌌 Delve into the physics of the super small—atoms and subatomic particles. Explore concepts like wave-particle duality and superposition, paving the way for quantum computing and revolutionary technology. Dive into the quantum frontier with confidence!"
    },
    {
        "question": "Define artificial intelligence, you say?",
        "response": "Experience the future of technology with our cutting-edge artificial intelligence product! 🤖 Dive into a branch of computer science dedicated to creating intelligent machines. Algorithms, machine learning, and neural networks converge to enable machines to learn, adapt, and make smart decisions. Join the AI revolution and embrace the possibilities!"
    }
]

    example_template = """
    Question: {query}
    Response: {answer}
    """

    example_prompt = PromptTemplate(
        input_variables= ["query","answer"],
        template= example_template
    )

    prefix = """You are a {age_option}, and {taskType_option}:
    Here are some examples:
    """

    suffix = """
    Question: {userInput}
    Response:
    """

    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=example_prompt,
        max_length=200
    )

    prompt_template = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["userInput","age_option","taskType_option"],
        example_separator="\n\n"
    )

    print(prompt_template.format(userInput= query, age_option= age_option, taskType_option = taskType_option))

    response = llm(prompt_template.format(userInput=query, age_option= age_option, taskType_option = taskType_option))
    print(response)

    return response


#UI Starts here
st.set_page_config(page_title="Marketing Tool",
                   page_icon="🚀",
                   layout="wide",
                   initial_sidebar_state="expanded"    
                   )


st.header("Hey, How can I help you!")

form_input = st.text_area("Enter Text", height=150)

taskType_option = st.selectbox(
    'Please select the action to be performed',
    ('Write a sales copy', 'Create a tweet', 'Write a product description'),
    key=1
)

age_option = st.selectbox(
    'For which age group?',
    ('Kid', 'Adult', 'Senior Citizen'),
    key=2
)

submit = st.button('Generate')

if submit:
    respond = getLLMResponse(form_input, age_option, taskType_option)
    # Find the index of the first occurrence of "Question" in the generated response
    index_of_question = respond.find("Question")

    # If "Question" is found, truncate the response to that point
    if index_of_question != -1:
        respond = respond[:index_of_question]
    
    st.write(respond)

