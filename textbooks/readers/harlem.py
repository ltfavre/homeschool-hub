"""Voices of the Harlem Renaissance: a VenvLearning anthology for Grade 7.
Background chapters are original VenvLearning writing. Every poem and essay excerpt was published in 1930 or earlier and is in
the public domain in the United States; texts are from the first editions as transcribed on Wikisource.
Section titles match the Grade 7 ELA lessons (Units 7 and 9)."""

SECTIONS = []


def sec(title, paras, selections=(), words=()):
    SECTIONS.append({"title": title, "paras": paras, "selections": list(selections), "words": list(words)})


def poem(title, author, source, text):
    return {"kind": "poem", "title": title, "author": author, "source": source, "text": text.strip("\n")}


def prose(title, author, source, paras, note="Excerpt"):
    return {"kind": "prose", "title": title, "author": author, "source": source, "paras": paras, "note": note}


sec("Introduction and a Note on Historical Language",
    ["In the 1920s, a neighborhood in the northern part of New York City called Harlem became the center of an explosion of art, music, writing, and ideas. Poets, novelists, painters, musicians, scholars, and journalists poured into Harlem from the American South, from the Caribbean, and from cities across the country. Together they created a movement that people at the time called the “New Negro” movement. Today we call it the Harlem Renaissance.",
     "The word renaissance means “rebirth.” It was first used for the great flowering of art and learning in Europe in the 1400s and 1500s. The writers and artists of Harlem were not reborn, of course. But many of them felt that something new was being born: a new confidence, a new pride, and a new determination to tell the story of Black life in America in their own words.",
     "The Harlem Renaissance did not happen all at once, and it did not happen only in Harlem. It grew out of decades of struggle and achievement. It was shaped by the Great Migration, by newspapers and magazines, by the music of jazz and the blues, and by writers who came before. It also reached far beyond New York, to cities such as Washington, D.C., and Chicago, and to readers around the world.",
     "In this Reader you will meet some of the people who made the movement and read some of their own words: poems, essays, and speeches written between 1895 and 1930.",
     "A note on historical language. The writers in this book lived about one hundred years ago, and they used the words for race that were common in their time. In the 1920s, the word Negro was the respectful, standard term, and many writers capitalized it proudly; the “New Negro” was a phrase of pride. Today we use the terms Black and African American, and Negro is considered out of date. You will also see at least one word, in Countee Cullen's poem “Incident,” that was meant as a cruel insult. Cullen used it on purpose, to show the hurt that a single hateful word can cause a child.",
     "When you read historical texts, read the words in their context: ask who is speaking, when, to whom, and why. Quote the texts accurately when you write about them, but use today's respectful terms in your own sentences and discussions. A slur is never acceptable to use in conversation, even when you are discussing a poem that contains one."],
    words=[("renaissance", "a rebirth; a time of new energy in art and learning"), ("movement", "a group of people working toward shared goals over time"),
           ("context", "the time, place, and situation in which something was written"), ("slur", "an insulting word used to hurt a group of people")])

sec("Literary Tradition and Paul Laurence Dunbar",
    ["The writers of the Harlem Renaissance did not appear out of nowhere. They built on a long literary tradition. In the 1700s, Phillis Wheatley, who had been brought to Boston as an enslaved child, became the first African American to publish a book of poetry. In the 1800s, Frederick Douglass wrote powerful accounts of his life in slavery and his escape to freedom. These writers showed that Black Americans could use the written word to tell the truth about their lives.",
     "One writer from the generation before the Harlem Renaissance was especially important to the poets who came later: Paul Laurence Dunbar. Dunbar was born in Dayton, Ohio, in 1872. His parents had been enslaved in Kentucky. In high school, he was the only Black student in his class, and he edited the school newspaper and wrote poems. After graduating, he could not find work as a writer because of racial prejudice, so he took a job running an elevator. Between rides, he wrote poetry.",
     "Dunbar published his first books himself and sold copies to his elevator passengers. In 1896, his collection Lyrics of Lowly Life, with an introduction by the famous critic William Dean Howells, made him one of the best-known poets in America. He was one of the first African American writers to earn national fame and to support himself by writing.",
     "Dunbar wrote in two different styles. Some of his poems were written in dialect, imitating the speech of Black Southerners. White audiences loved these poems, and they made him famous. But many of his most powerful poems were written in standard English. In these poems he wrote about pain, pride, and the hidden feelings of people forced to smile in the face of injustice. Dunbar was sometimes frustrated that critics praised his dialect poems and paid less attention to his other work.",
     "Dunbar died of tuberculosis in 1906, when he was only thirty-three. But the poets of the Harlem Renaissance read his work and saw him as a forerunner, a writer who had opened the door for them. His poem “Sympathy,” about a caged bird, later gave the writer Maya Angelou the title for her famous memoir, I Know Why the Caged Bird Sings."],
    [poem("We Wear the Mask", "Paul Laurence Dunbar", "Lyrics of Lowly Life (1896)", """
We wear the mask that grins and lies,
It hides our cheeks and shades our eyes,—
This debt we pay to human guile;
With torn and bleeding hearts we smile,
And mouth with myriad subtleties.

Why should the world be over-wise,
In counting all our tears and sighs?
Nay, let them only see us, while
  We wear the mask.

We smile, but, O great Christ, our cries
To thee from tortured souls arise.
We sing, but oh the clay is vile
Beneath our feet, and long the mile;
But let the world dream otherwise,
  We wear the mask!
"""),
     poem("Sympathy", "Paul Laurence Dunbar", "Lyrics of the Hearthside (1899)", """
I know what the caged bird feels, alas!
   When the sun is bright on the upland slopes;
When the wind stirs soft through the springing grass,
And the river flows like a stream of glass;
   When the first bird sings and the first bud opes,
And the faint perfume from its chalice steals--
I know what the caged bird feels!

I know why the caged bird beats his wing
   Till its blood is red on the cruel bars;
For he must fly back to his perch and cling
When he fain would be on the bough a-swing;
   And a pain still throbs in the old, old scars
And they pulse again with a keener sting--
I know why he beats his wing!

I know why the caged bird sings, ah me,
   When his wing is bruised and his bosom sore,--
When he beats his bars and he would be free;
It is not a carol of joy or glee,
   But a prayer that he sends from his heart's deep core,
But a plea, that upward to Heaven he flings--
I know why the caged bird sings!
""")],
    words=[("dialect", "a way of speaking that belongs to a particular region or group"), ("forerunner", "someone who comes before and prepares the way"),
           ("guile", "clever trickery"), ("myriad", "countless; a great many")])

sec("The Great Migration and Charles S. Johnson",
    ["Around 1915, one of the largest movements of people in American history began. Over the next several decades, about six million Black Americans left the rural South and moved to cities in the North, the Midwest, and the West. Historians call this the Great Migration.",
     "People left the South for many reasons. Historians sometimes divide these reasons into push factors, which pushed people out, and pull factors, which pulled them toward a new place. Push factors included the unfair Jim Crow laws that enforced segregation and kept Black Southerners from voting, the constant threat of violence, and hard times on Southern farms, where a tiny insect called the boll weevil destroyed cotton crops. Pull factors included jobs in Northern factories, which needed workers when World War I cut off immigration from Europe, better schools, and the hope of greater freedom.",
     "Many migrants learned about life in the North from Black newspapers, which printed job advertisements and letters from people who had already moved. Families often traveled north by train, carrying everything they owned. They settled in cities such as Chicago, Detroit, Philadelphia, Pittsburgh, and New York.",
     "In New York, many settled in Harlem. By the 1920s, Harlem had become the largest Black community in the United States. Newcomers from the South lived alongside immigrants from Jamaica, Barbados, Haiti, and other Caribbean islands. The mix of people, experiences, and ideas helped make Harlem a place of tremendous creative energy. The Jamaican-born poet Claude McKay, who came to the United States in 1912, captured the homesickness that many newcomers felt in his poem “The Tropics in New York.”",
     "One person who understood the importance of the Great Migration was Charles S. Johnson. Johnson, born in Virginia in 1893, was a sociologist, a scientist who studies how people live in groups. After serving in World War I, he studied the Black migrants who had moved to Chicago and helped write a major report on race relations there after a deadly riot in 1919.",
     "In 1923, Johnson became the first editor of Opportunity: A Journal of Negro Life, the magazine of the National Urban League. Johnson believed that art and literature could change the way Americans saw one another. He used Opportunity to publish young writers, and in 1924 he began holding literary contests with cash prizes. Langston Hughes, Countee Cullen, and Zora Neale Hurston were among the early prizewinners. In March 1924, Johnson organized a dinner at the Civic Club in New York where young Black writers were introduced to publishers and editors. Many historians see that evening as one of the starting points of the Harlem Renaissance.",
     "Johnson later became a leading scholar of race in America, and in 1946 he became the first Black president of Fisk University in Nashville, Tennessee."],
    [poem("The Tropics in New York", "Claude McKay", "Harlem Shadows (1922)", """
Bananas ripe and green, and ginger-root,
Cocoa in pods and alligator pears,
And tangerines and mangoes and grape fruit,
Fit for the highest prize at parish fairs,

Set in the window, bringing memories
Of fruit-trees laden by low-singing rills,
And dewy dawns, and mystical blue skies
In benediction over nun-like hills.

My eyes grew dim, and I could no more gaze;
A wave of longing through my body swept,
And, hungry for the old, familiar ways,
I turned aside and bowed my head and wept.
""")],
    words=[("migration", "the movement of people from one place to another"), ("segregation", "the separation of people by race"),
           ("sociologist", "a scientist who studies how people live in groups"), ("benediction", "a blessing")])

sec("Harlem, the Black Press, and J. A. Rogers",
    ["Newspapers and magazines were the internet of the 1920s. They carried news, opinions, poems, stories, and advertisements to readers across the country. For Black Americans, the Black press was especially important. Mainstream white newspapers often ignored Black communities or wrote about them unfairly. Black newspapers and magazines told the stories that others left out.",
     "In 1905, Robert S. Abbott founded the Chicago Defender. Abbott's newspaper reported on injustice in the South and described the opportunities waiting in the North. Railroad porters carried copies of the Defender south on the trains, and it was passed from hand to hand and read aloud in churches and barbershops. The Defender helped encourage the Great Migration.",
     "In 1910, the scholar W. E. B. Du Bois became the editor of The Crisis, the magazine of the NAACP, the National Association for the Advancement of Colored People. Du Bois used The Crisis to fight for civil rights, and he also used it to publish poetry and fiction. The Crisis published Langston Hughes's first famous poem, “The Negro Speaks of Rivers,” in 1921. Its literary editor, Jessie Redmon Fauset, discovered and encouraged many young writers. Along with Charles S. Johnson's Opportunity, The Crisis gave the writers of the Harlem Renaissance a place to be read.",
     "Journalists also worked to recover a history that had been ignored. J. A. Rogers, born in Jamaica around 1880, came to the United States as a young man. He worked as a railroad porter and spent his free time in libraries, researching the achievements of people of African descent throughout history. He became a columnist for the Pittsburgh Courier, one of the most widely read Black newspapers, and wrote books challenging the claim that Black people had no history worth studying. In 1925 he contributed an essay about jazz to The New Negro.",
     "Rogers was part of a larger effort to “dig up” the past. The book collector Arthur A. Schomburg, born in Puerto Rico, gathered thousands of books, pamphlets, and documents about Black history from around the world. His collection became the foundation of what is now the Schomburg Center for Research in Black Culture, part of the New York Public Library, which still stands in Harlem today. In an essay published in 1925, Schomburg explained why this work mattered."],
    [prose("The Negro Digs Up His Past", "Arthur A. Schomburg", "The New Negro (1925)", [
        "The American Negro must remake his past in order to make his future. Though it is orthodox to think of America as the one country where it is unnecessary to have a past, what is a luxury for the nation as a whole becomes a prime social necessity for the Negro. For him, a group tradition must supply compensation for persecution, and pride of race the antidote for prejudice. History must restore what slavery took away, for it is the social damage of slavery that the present generations must repair and offset.",
        "Gradually as the study of the Negro’s past has come out of the vagaries of rhetoric and propaganda and become systematic and scientific, three outstanding conclusions have been established:",
        "First, that the Negro has been throughout the centuries of controversy an active collaborator, and often a pioneer, in the struggle for his own freedom and advancement. This is true to a degree which makes it the more surprising that it has not been recognized earlier.",
        "Second, that by virtue of their being regarded as something \"exceptional,” even by friends and well-wishers, Negroes of attainment and genius have been unfairly disassociated from the group, and group credit lost accordingly.",
        "Third, that the remote racial origins of the Negro, far from being what the race and the world have been given to understand, offer a record of credible group achievement when scientifically viewed, and more important still, that they are of vital general interest because of their bearing upon the beginnings and early development of human culture.",
        "With such crucial truths to document and establish, an ounce of fact is worth a pound of controversy."])],
    words=[("press", "newspapers and magazines, and the people who write them"), ("columnist", "a writer who regularly writes articles for a newspaper"),
           ("descent", "family origin; ancestry"), ("antidote", "a remedy; something that cures a poison")])

sec("The New Negro: Locke and Kellogg",
    ["In March 1925, a magazine called Survey Graphic published a special issue with the title Harlem: Mecca of the New Negro. Survey Graphic was a magazine about social issues, and its editor, Paul Kellogg, was a white reformer who wanted Americans to understand the changes happening in their country. Kellogg invited a Black scholar to serve as guest editor of the issue: Alain Locke.",
     "Locke, born in Philadelphia in 1885, was a philosopher who taught at Howard University in Washington, D.C. In 1907 he had become the first African American Rhodes Scholar, earning the chance to study at Oxford University in England. Locke believed that the young Black writers and artists of the 1920s were creating something new and important, and he wanted the rest of the country to see it.",
     "The Harlem issue of Survey Graphic included essays, poems, stories, and portraits by Black writers and artists. It was so popular that the magazine had to print extra copies. Later in 1925, Locke expanded it into a book called The New Negro: An Interpretation. The New Negro collected poetry by Langston Hughes, Countee Cullen, Claude McKay, and Georgia Douglas Johnson; stories by Zora Neale Hurston and Jean Toomer; essays on history, music, art, and education; and illustrations by the artist Aaron Douglas. It became the defining book of the Harlem Renaissance.",
     "In his title essay, Locke argued that a “New Negro” had arrived: Black Americans who refused to accept old stereotypes, who were proud of their heritage, and who spoke for themselves. For generations, he wrote, Black Americans had been treated as “a problem” to be argued about rather than as people. Now, through art and self-expression, they were defining themselves.",
     "Not everyone agreed with every part of Locke's vision. Some critics, including W. E. B. Du Bois, believed that art should be used more directly as a tool in the fight for civil rights. Others worried that white publishers and audiences were more interested in entertainment than in the truth about Black life. These debates were part of what made the Harlem Renaissance so lively."],
    [prose("The New Negro", "Alain Locke", "The New Negro (1925)", [
        "In the last decade something beyond the watch and guard of statistics has happened in the life of the American Negro and the three norns who have traditionally presided over the Negro problem have a changeling in their laps. The Sociologist, the Philanthropist, the Race-leader are not unaware of the New Negro, but they are at a loss to account for him. He simply cannot be swathed in their formulæ. For the younger generation is vibrant with a new psychology; the new spirit is awake in the masses, and under the very eyes of the professional observers is transforming what has been a perennial problem into the progressive phases of contemporary Negro life.",
        "Recall how suddenly the Negro spirituals revealed themselves; suppressed for generations under the stereotypes of Wesleyan hymn harmony, secretive, half-ashamed, until the courage of being natural brought them out—and behold, there was folk-music. Similarly the mind of the Negro seems suddenly to have slipped from under the tyranny of social intimidation and to be shaking off the psychology of imitation and implied inferiority. By shedding the old chrysalis of the Negro problem we are achieving something like a spiritual emancipation. Until recently, lacking self-understanding, we have been almost as much of a problem to ourselves as we still are to others. But the decade that found us with a problem has left us with only a task. The multitude perhaps feels as yet only a strange relief and a new vague urge, but the thinking few know that in the reaction the vital inner grip of prejudice has been broken."]),
     prose("Negro Youth Speaks", "Alain Locke", "The New Negro (1925)", [
        "The Younger Generation comes, bringing its gifts. They are the first fruits of the Negro Renaissance. Youth speaks, and the voice of the New Negro is heard. What stirs inarticulately in the masses is already vocal upon the lips of the talented few, and the future listens, however the present may shut its ears.",
        "Our poets have now stopped speaking for the Negro—they speak as Negroes. Where formerly they spoke to others and tried to interpret, they now speak to their own and try to express. They have stopped posing, being nearer the attainment of poise."])],
    words=[("stereotype", "an oversimplified, often unfair idea about a group of people"), ("norns", "in Norse myth, three women who control fate"),
           ("changeling", "in folk tales, a child secretly swapped for another"), ("chrysalis", "the case a caterpillar forms before becoming a butterfly")])

sec("Langston Hughes",
    ["Of all the writers of the Harlem Renaissance, the one most often read today is Langston Hughes. Hughes was born in Joplin, Missouri, in 1901, and grew up mostly in Lawrence, Kansas, with his grandmother, and later in Cleveland, Ohio. His grandmother told him stories of heroes who had fought against slavery, and he read every book he could find.",
     "When Hughes was about eighteen, he took a train across the Mississippi River on his way to visit his father in Mexico. Looking out at the great muddy river at sunset, he thought about the rivers that had been part of Black history: the Euphrates, the Congo, the Nile, and the Mississippi. On the back of an envelope, he wrote “The Negro Speaks of Rivers.” The Crisis published it in 1921, and it made him known.",
     "Hughes moved to Harlem, worked at many jobs, and traveled the world as a sailor. In 1925, his poem “The Weary Blues” won first prize in Opportunity's poetry contest, and in 1926 his first book of poems, also called The Weary Blues, was published. Hughes was one of the first poets to use the rhythms of jazz and the blues in poetry. He wanted his poems to sound like the music and speech of ordinary Black people, not just educated readers.",
     "In a 1926 essay, Hughes declared that young Black artists should express themselves “without fear or shame.” He wrote poems, novels, short stories, plays, newspaper columns, and books for children for more than forty years. He died in 1967. His home in Harlem still stands, and his poems are read in classrooms around the world."],
    [poem("The Negro Speaks of Rivers", "Langston Hughes", "The Weary Blues (1926); first published in The Crisis (1921)", """
(To W. E. B. DuBois)

I've known rivers:
I've known rivers ancient as the world and older than the flow of human blood in human veins.

My soul has grown deep like the rivers.

I bathed in the Euphrates when dawns were young.
I built my hut near the Congo and it lulled me to sleep.
I looked upon the Nile and raised the pyramids above it.
I heard the singing of the Mississippi when Abe Lincoln went down to New Orleans, and I've seen its muddy bosom turn all golden in the sunset.

I've known rivers:
Ancient, dusky rivers.

My soul has grown deep like the rivers.
"""),
     poem("Mother to Son", "Langston Hughes", "The Weary Blues (1926)", """
Well, son, I'll tell you:
Life for me ain't been no crystal stair.
It's had tacks in it,
And splinters,
And boards torn up,
And places with no carpet on the floor—
Bare.
But all the time
I'se been a-climbin' on,
And reachin' landin's,
And turnin' corners,
And sometimes goin' in the dark
Where there ain't been no light.
So boy, don't you turn back.
Don't you set down on the steps
'Cause you finds it's kinder hard.
Don't you fall now—
For I'se still goin', honey,
I'se still climbin',
And life for me ain't been no crystal stair.
"""),
     poem("Dream Variation", "Langston Hughes", "The Weary Blues (1926)", """
To fling my arms wide
In some place of the sun,
To whirl and to dance
Till the white day is done.
Then rest at cool evening
Beneath a tall tree
While night comes on gently,
Dark like me,—
That is my dream!

To fling my arms wide
In the face of the sun,
Dance! whirl! whirl!
Till the quick day is done.
Rest at pale evening. . . .
A tall, slim tree. . . .
Night coming tenderly
Black like me.
"""),
     poem("The Dream Keeper", "Langston Hughes", "The Weary Blues (1926)", """
Bring me all of your dreams,
You dreamers.
Bring me all of your
Heart melodies
That I may wrap them
In a blue cloud-cloth
Away from the too rough fingers
Of the world.
"""),
     poem("Epilogue (“I, Too”)", "Langston Hughes", "The Weary Blues (1926)", """
I, too, sing America.

I am the darker brother.
They send me to eat in the kitchen
When company comes,
But I laugh,
And eat well,
And grow strong.

Tomorrow,
I'll sit at the table
When company comes.
Nobody'll dare
Say to me,
"Eat in the kitchen,"
Then.

Besides,
They'll see how beautiful I am
And be ashamed,—

I, too, am America.
"""),
     poem("The Weary Blues", "Langston Hughes", "The Weary Blues (1926)", """
Droning a drowsy syncopated tune,
Rocking back and forth to a mellow croon,
I heard a Negro play.
Down on Lenox Avenue the other night
By the pale dull pallor of an old gas light
He did a lazy sway. . . .
He did a lazy sway. . . .
To the tune o' those Weary Blues.
With his ebony hands on each ivory key
He made that poor piano moan with melody.
O Blues!
Swaying to and fro on his rickety stool
He played that sad raggy tune like a musical fool.
Sweet Blues!
Coming from a black man's soul.
O Blues!
In a deep song voice with a melancholy tone
I heard that Negro sing, that old piano moan—
"Ain't got nobody in all this world,
Ain't got nobody but ma self.
I's gwine to quit ma frownin'
And put ma troubles on the shelf."
Thump, thump, thump, went his foot on the floor.
He played a few chords then he sang some more—
"I got the Weary Blues
And I can't be satisfied.
Got the Weary Blues
And can't be satisfied—
I ain't happy no mo'
And I wish that I had died."

And far into the night he crooned that tune.
The stars went out and so did the moon.
The singer stopped playing and went to bed
While the Weary Blues echoed through his head.
He slept like a rock or a man that's dead.
""")],
    words=[("syncopated", "with the beat shifted to unexpected places, as in jazz"), ("croon", "to sing softly"),
           ("melancholy", "sad and thoughtful"), ("variation", "a different version of something")])

sec("Georgia Douglas Johnson",
    ["Georgia Douglas Johnson was one of the first Black women poets to win national attention in the twentieth century. She was born in Atlanta, Georgia, around 1877, studied at Atlanta University, and also studied music at Oberlin Conservatory in Ohio. In 1910 she moved with her husband to Washington, D.C., where she lived for the rest of her life.",
     "Johnson published her first book of poems, The Heart of a Woman, in 1918. Its poems explored the feelings and hopes of women, and especially the dreams that women were often not free to follow. Her second book, Bronze (1922), focused on race and on the experiences of Black mothers. A third book, An Autumn Love Cycle, followed in 1928. She also wrote many plays. Her play Plumes won first prize in Opportunity's contest in 1927.",
     "Johnson is also remembered for what happened in her home. Her house at 1461 S Street NW in Washington, which she called the Half-Way House, became a gathering place for writers and artists. On Saturday nights, poets and thinkers such as Langston Hughes, Jean Toomer, Countee Cullen, Alain Locke, Jessie Redmon Fauset, Angelina Weld Grimké, and Zora Neale Hurston came to read their work, share ideas, and encourage one another. This gathering became known as the S Street Salon.",
     "Johnson worked at government jobs to support her two sons after her husband died in 1925, and she wrote late at night. She continued writing for the rest of her long life. She died in 1966. Her life shows that the Harlem Renaissance was not only a New York story, and that its writers depended on friendship, community, and generous hosts."],
    [poem("The Heart of a Woman", "Georgia Douglas Johnson", "The Heart of a Woman and Other Poems (1918)", """
The heart of a woman goes forth with the dawn,
As a lone bird, soft winging, so restlessly on,
Afar o'er life's turrets and vales does it roam
In the wake of those echoes the heart calls home.

The heart of a woman falls back with the night,
And enters some alien cage in its plight,
And tries to forget it has dreamed of the stars
While it breaks, breaks, breaks on the sheltering bars.
"""),
     poem("Calling Dreams", "Georgia Douglas Johnson", "Bronze (1922)", """
The right to make my dreams come true
I ask, nay, I demand of life,
Nor shall fate's deadly contraband
Impede my steps, nor countermand.

Too long my heart against the ground
Has beat the dusty years around,
And now, at length, I rise, I wake!
And stride into the morning-break!
""")],
    words=[("salon", "a regular gathering of writers and thinkers in someone's home"), ("turrets", "small towers"),
           ("contraband", "goods forbidden by law; here, things that block the way"), ("countermand", "to cancel an order")])

sec("Elise Johnson McDougald",
    ["Not every voice of the Harlem Renaissance belonged to a poet or a novelist. Elise Johnson McDougald was an educator, a social researcher, and a writer who spent her life working for children, workers, and women in Harlem.",
     "McDougald was born in Manhattan in 1885. She became a teacher in New York City's public schools in 1905. She also worked to improve the lives of working people. She studied the working conditions of Black women in New York, helped organize laundry workers, and served as a vocational counselor, helping young people find jobs that matched their skills.",
     "In March 1925, McDougald wrote an essay for the Harlem issue of Survey Graphic called “The Double Task: The Struggle of Negro Women for Sex and Race Emancipation.” Alain Locke included a version of it, titled “The Task of Negro Womanhood,” in The New Negro later that year. In her essay, McDougald described the “double task” facing Black women: they had to struggle against unfair treatment both because they were women and because they were Black. She described Black women in many kinds of work, from domestic workers and factory workers to teachers, nurses, business owners, and writers, and she argued that their contributions deserved respect.",
     "McDougald's own career showed what she meant. In the 1930s she became the principal of P.S. 24 in Harlem and is often described as the first Black woman to serve as a principal in a New York City public school. One of her students there was the future writer James Baldwin. She later led P.S. 119 until she retired in 1954. After retiring, she wrote a newspaper column about Harlem's schools.",
     "When you read about the Harlem Renaissance, remember McDougald's point: a movement is made not only by famous artists but also by the many people who teach, organize, and build the community that artists depend on."],
    words=[("emancipation", "freedom from control or unfair limits"), ("vocational", "relating to jobs and careers"),
           ("domestic worker", "a person paid to clean, cook, or care for children in someone's home"), ("principal", "the leader of a school")])

sec("More Voices of the Harlem Renaissance",
    ["The Harlem Renaissance included many more writers than one Reader can hold. Here are a few more voices.",
     "Claude McKay (about 1889–1948) was born in Jamaica and came to the United States in 1912. In 1919, a summer of violent attacks on Black communities across the United States, he wrote “If We Must Die,” a sonnet calling for courage and dignity in the face of attack. His collection Harlem Shadows (1922) is often seen as one of the first books of the Harlem Renaissance.",
     "Countee Cullen (1903–1946) grew up in New York City and was a star student at New York University and Harvard. He loved traditional poetic forms such as the sonnet. His first book, Color, was published in 1925, when he was only twenty-two. “Incident” describes a moment from his childhood in just twelve lines; “Yet Do I Marvel” is a sonnet about faith, suffering, and the gift of poetry. Cullen later taught English and French at a junior high school in New York City.",
     "Zora Neale Hurston (1891–1960) grew up in Eatonville, Florida, one of the first all-Black towns in the United States to be incorporated. She studied anthropology and collected the folktales and songs of Black communities in the South. Her stories, essays, and later her novel Their Eyes Were Watching God (1937) captured the voices of the people she grew up with."],
    [poem("If We Must Die", "Claude McKay", "Harlem Shadows (1922); first published 1919", """
If we must die, let it not be like hogs
Hunted and penned in an inglorious spot,
While round us bark the mad and hungry dogs,
Making their mock at our accursèd lot.
If we must die, O let us nobly die,
So that our precious blood may not be shed
In vain; then even the monsters we defy
Shall be constrained to honor us though dead!
O kinsmen! we must meet the common foe!
Though far outnumbered let us show us brave,
And for their thousand blows deal one death-blow!
What though before us lies the open grave?
Like men we'll face the murderous, cowardly pack,
Pressed to the wall, dying, but fighting back!
"""),
     poem("Incident", "Countee Cullen", "Color (1925)", """
(for Eric Walrond)

Once riding in old Baltimore,
Heart-filled, head-filled with glee,
I saw a Baltimorean
 Keep looking straight at me.

Now I was eight and very small,
 And he was no whit bigger,
And so I smiled, but he poked out
 His tongue, and called me, “Nigger.”

I saw the whole of Baltimore
 From May until December;
Of all the things that happened there
 That’s all that I remember.
"""),
     poem("Yet Do I Marvel", "Countee Cullen", "Color (1925)", """
I doubt not God is good, well-meaning, kind,
And did He stoop to quibble could tell why
The little buried mole continues blind,
Why flesh that mirrors Him must some day die,
Make plain the reason tortured Tantalus
Is baited by the fickle fruit, declare
If merely brute caprice dooms Sisyphus
To struggle up a never-ending stair.
Inscrutable His ways are, and immune
To catechism by a mind too strewn
With petty cares to slightly understand
What awful brain compels His awful hand.
Yet do I marvel at this curious thing:
To make a poet black, and bid him sing!
""")],
    words=[("sonnet", "a fourteen-line poem with a set rhyme pattern"), ("anthropology", "the study of human cultures"),
           ("Tantalus, Sisyphus", "figures in Greek myth punished forever: one never reaching food, one forever pushing a rock uphill"),
           ("inscrutable", "impossible to understand")])
