from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# text="""
# The Game of Cricket: A Timeless Classic

# Cricket, often referred to as the "gentleman's game," is a sport that has been a cornerstone of international competition for over a century. With a rich history, intricate rules, and a massive global following, cricket has become an integral part of many cultures around the world.

# Origins and Evolution

# The modern game of cricket originated in England in the 16th century, with the first recorded match taking place in 1598. The game evolved over the centuries, with the first official rules being published in 1744. Cricket was initially played by the upper class, but it soon spread to the masses, becoming a popular sport among the working class.

# The Basics

# Cricket is a bat-and-ball game played between two teams, each consisting of eleven players. The objective is simple: score runs by hitting the ball with a bat, while the opposing team tries to stop you by getting you out. A match is typically divided into innings, with each team taking turns to bat and bowl.

# Types of Cricket

# There are several forms of cricket, each with its unique characteristics:

# Test Cricket: The longest and most traditional form of the game, played over several days.
# One-Day Internationals (ODIs): A shorter version of the game, played in one day.
# Twenty20 (T20): A fast-paced, condensed version of the game, played in about three hours.
# Global Reach and Popularity

# Cricket is the second-most popular sport in the world, in terms of viewership, with an estimated 2.5 billion fans globally. The sport is particularly popular in the Indian subcontinent, the Caribbean, and the United Kingdom. The Indian Premier League (IPL) and the International Cricket Council (ICC) World Cup are two of the most-watched sporting events in the world.

# The Impact of Cricket

# Cricket has had a significant impact on society, transcending the realm of sports. It has:

# Promoted international relations: Cricket has played a crucial role in fostering diplomatic relations between nations, particularly during times of conflict.
# Inspired social change: Cricket has been a platform for social commentary, with players and teams using their influence to raise awareness about social issues.
# Developed infrastructure: The construction of cricket stadiums and facilities has contributed to the development of infrastructure in many countries.
# Conclusion

# Cricket is a sport that has captivated the hearts of millions around the world. Its rich history, intricate rules, and global reach have made it a timeless classic. As the game continues to evolve, it remains an integral part of many cultures, inspiring social change, promoting international relations, and entertaining fans worldwide.
# """


loader = PyPDFLoader("DROW.pdf")
docs =loader.load()

splitter =CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)




result=splitter.split_documents(docs)
# print(result)

print(len(result))
print(result[0].page_content)
print(result[1].metadata)