 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

#Open the SQLite database file and start a database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
database_session = DBSession()


#Create dummy user
user = User(name="Aministrator", email="admin@my.catalog.udacity.com", picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
database_session.add(user)
database_session.commit()

#Category for Spain
spain = Category(name = "Spanish La Liga", description=u"The Primera División of the Liga Nacional de Fútbol Profesional, commonly known in the English-speaking world as La Liga, is the top professional association football division of the Spanish football league system.", image_url = "http://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Liga_BBVA.svg/320px-Liga_BBVA.svg.png")
database_session.add(spain)
database_session.commit()

#Add 4 teams to 'Spanish La Liga' category
database_session.add(Item(user_id=1, name = "Real Madrid C.F.", description = u"Real Madrid Club de Fútbol, commonly known as Real Madrid, or simply as Real, is a professional football club based in Madrid, Spain.Founded in 1902 as Madrid Football Club, the team has traditionally worn a white home kit since. The word Real is Spanish for Royal and was bestowed to the club by King Alfonso XIII in 1920 together with the royal crown in the emblem. The team has played its home matches in the 81,044-capacity Santiago Bernabéu Stadium in downtown Madrid since 1947. Unlike most European football clubs, Real Madrid's members (socios) have owned and operated the club since its inception.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/343px-Real_Madrid_CF.svg.png", category = spain))
database_session.commit()
database_session.add(Item(user_id=1, name = "FC Barcelona", description = u"Futbol Club Barcelona, also known as Barcelona and familiarly as Barça, is a professional football club, based in Barcelona, Catalonia, Spain. Founded in 1899 by a group of Swiss, English and Catalan footballers led by Joan Gamper, the club has become a symbol of Catalan culture and Catalanism, hence the motto \"Més que un club\" (More than a club). Unlike many other football clubs, the supporters own and operate Barcelona.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/237px-FC_Barcelona_%28crest%29.svg.png", category = spain))
database_session.commit()
database_session.add(Item(user_id=1, name = "Atletico Madrid", description = u"Club Atlético de Madrid, SAD, commonly known as Atlético de Madrid or Atlético, is a Spanish professional football club based in Madrid that plays in La Liga, where they are the current champions. In terms of the number of titles, Atlético Madrid is the fourth most successful club in Spanish Football behind Real Madrid CF, FC Barcelona and Athletic Bilbao.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/c/c1/Atletico_Madrid_logo.svg/375px-Atletico_Madrid_logo.svg.png", category = spain))
database_session.commit()
database_session.add(Item(user_id=1, name = "Valencia CF", description = u"Valencia Club de Fútbol are a Spanish football club based in Valencia. They play in La Liga and are one of the most successful and biggest clubs in Spanish football and European football. Valencia have won six La Liga titles, seven Copa del Rey trophies, two Fairs Cups (which was the predecessor to the UEFA Cup), one UEFA Cup, one UEFA Cup Winners' Cup, and two UEFA Super Cups. They also reached two UEFA Champions League finals in a row, losing to La Liga rivals Real Madrid in 2000 and then to German club Bayern Munich on penalties after a 1–1 draw in 2001.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Valenciacf.svg/380px-Valenciacf.svg.png", category = spain))
database_session.commit()

#Category for England
england = Category(name = "English Premier League", description="The Premier League is an English professional league for men's association football clubs. At the top of the English football league system, it is the country's primary football competition.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/5/5a/Premier_League.svg/169px-Premier_League.svg.png")
database_session.add(england)
database_session.commit()

#Add 4 teams to 'English Premier League' category
database_session.add(Item(user_id=1, name = "Manchester United F.C.", description = u"Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England, that plays in the Premier League. Founded as Newton Heath LYR Football Club in 1878, the club changed its name to Manchester United in 1902 and moved to Old Trafford in 1910.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Manchester_United_FC_crest.svg/237px-Manchester_United_FC_crest.svg.png", category = england))
database_session.commit()
database_session.add(Item(user_id=1, name = "Arsenal F.C.", description = u"Arsenal Football Club is a professional football club based in Holloway, London that plays in English football's top tier, the Premier League. One of the most decorated clubs in English football, they have won 13 First Division and Premier League titles and a joint record 11 FA Cups.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/5/53/Arsenal_FC.svg/323px-Arsenal_FC.svg.png", category = england))
database_session.commit()
database_session.add(Item(user_id=1, name = "Chelsea F.C.", description = u"Chelsea Football Club are a professional football club based in Fulham, London, who play in the Premier League, the highest level of English football. Founded in 1905, the club have spent most of their history in the top tier of English football. The club's home ground is the 41,837-seat Stamford Bridge stadium, where they have played since their establishment.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Chelsea_FC.svg/240px-Chelsea_FC.svg.png", category = england))
database_session.commit()
database_session.add(Item(user_id=1, name = "Liverpool F.C.", description = u"Liverpool Football Club is a Premier League football club based in Liverpool. The club have won more European trophies than any other English team with five European Cups, three UEFA Cups and three UEFA Super Cups. They have also won eighteen League titles, seven FA Cups and a record eight League Cups, although they are yet to win a Premier League title since its inception in 1992.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Liverpool_FC.svg/370px-Liverpool_FC.svg.png", category = england))
database_session.commit()

#Category for Germany
germany = Category(name = "German Bundesliga", description=u"The Bundesliga, is a professional association football league in Germany and the football league with the highest average stadium attendance worldwide. At the top of the German football league system, the Bundesliga is Germany's primary football competition.", image_url="http://upload.wikimedia.org/wikipedia/en/thumb/1/15/Bundesliga_logo.svg/272px-Bundesliga_logo.svg.png")
database_session.add(germany)
database_session.commit()

#Add 4 teams to 'German Bundesliga' category
database_session.add(Item(user_id=1, name = "FC Bayern Munich", description = u"Fußball-Club Bayern München e.V., commonly known as FC Bayern München, FCB, Bayern Munich, or FC Bayern, is a German sports club based in Munich, Bavaria. It is best known for its professional football team, which plays in the Bundesliga, the top tier of the German football league system, and is the most successful club in German football history, having won a record 25 national titles and 17 national cups.", image_url = "http://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Logo_FC_Bayern_M%C3%BCnchen.svg/480px-Logo_FC_Bayern_M%C3%BCnchen.svg.png", category = germany))
database_session.commit()
database_session.add(Item(user_id=1, name = "Borussia Dortmund", description = u"Ballspielverein Borussia 09 e.V. Dortmund, commonly known as Borussia Dortmund, Dortmund, or BVB, is a German sports club based in Dortmund, North Rhine-Westphalia. The football team is part of a large membership-based sports club with more than 115,000 members, making BVB the third largest sports club by membership in Germany. Dortmund plays in the Bundesliga, the top tier of the German football league system. Dortmund is one of the most successful clubs in German football history.", image_url = "http://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Borussia_Dortmund_logo.svg/240px-Borussia_Dortmund_logo.svg.png", category = germany))
database_session.commit()
database_session.add(Item(user_id=1, name = "Bayer Leverkusen", description = u"Bayer 04 Leverkusen, also known as Bayer Leverkusen, Leverkusen or simply Bayer, is a German football club based in Leverkusen, North Rhine-Westphalia. The club plays in the Bundesliga, the top tier of the German football league system, and host matches at the BayArena. The club was founded in 1904 by employees of the German pharmaceutical company Bayer, whose headquarters are in Leverkusen and from which the club draws its name. It was formerly the best-known department of TSV Bayer 04 Leverkusen, a sports club whose members also participate in athletics, gymnastics, basketball and other sports including the RTHC Bayer Leverkusen (rowing, tennis and hockey). In 1999 the football department was separated from the sports club and is now a separate entity formally called Bayer 04 Leverkusen GmbH.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/5/59/Bayer_04_Leverkusen_logo.svg/315px-Bayer_04_Leverkusen_logo.svg.png", category = germany))
database_session.commit()
database_session.add(Item(user_id=1, name = "FC Schalke 04", description = u"Fußballclub Gelsenkirchen-Schalke 04 e. V., commonly known as FC Schalke 04 or simply abbreviated as S04, is a professional German association-football club and multi-sports club originally from the Schalke district of Gelsenkirchen, North Rhine-Westphalia. Schalke has long been one of the most popular professional football teams and multi-sports club in Germany, even though major successes have been rare since the club's heyday in the 1930s and early 1940s. Schalke play in the Bundesliga, the top tier of the German football league system. The elite professionalism in association football team as of August 2014 is the biggest part of a large multi-sports club with 129,672 members (as of March 2014) making it the second-largest sports club in Germany and the third-largest sports club in the world in terms of membership, after the world’s second and first, rivals FC Bayern Munich and SL Benfica.", image_url = "http://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Schalke_04.svg/478px-Schalke_04.svg.png", category = germany))
database_session.commit()

#Category for Italy
italy = Category(name = "Italian Serie A", description=u"Serie A is a professional league competition for soccer clubs located at the top of the Italian football league system and has been operating for over eighty years since the 1929–30 season.", image_url = "http://upload.wikimedia.org/wikipedia/en/f/f7/LegaSerieAlogoTIM.png")
database_session.add(italy)
database_session.commit()

#Add 4 teams to 'Italian Serie A' category
database_session.add(Item(user_id=1, name = "Juventus F.C.", description = u"Juventus Football Club S.p.A., commonly referred to as Juventus and colloquially as Juve, are a professional Italian association football club based in Turin, Piedmont. The club is the third oldest of its kind in the country and has spent the majority of its history, with the exception of the 2006–07 season, in the top flight First Division (known as Serie A since 1929).", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Juventus_Turin.svg/294px-Juventus_Turin.svg.png", category = italy))
database_session.commit()
database_session.add(Item(user_id=1, name = "A.C. Milan", description = u"Associazione Calcio Milan, commonly referred to as A.C. Milan or simply Milan, is a professional Italian football club based in Milan, Lombardy, that plays in Serie A. Milan was founded in 1899 by English lace-maker Herbert Kilpin and businessman Alfred Edwards among others. The club has spent its entire history, with the exception of the 1980–81 and 1982–83 seasons, in the top flight of Italian football, known as Serie A since 1929–30.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/d/db/AC_Milan.svg/297px-AC_Milan.svg.png", category = italy))
database_session.commit()
database_session.add(Item(user_id=1, name = "Inter Milan", description = u"F.C. Internazionale Milano, commonly referred to as Internazionale or simply Inter, and colloquially known as Inter Milan outside of Italy, is a professional Italian football club based in Milan, Lombardy. They are the only club to have spent their entire history in the top flight of Italian football, known as Serie A, which started in 1929–30.", image_url = "http://upload.wikimedia.org/wikipedia/en/2/23/Inter_Milan.png", category = italy))
database_session.commit()
database_session.add(Item(user_id=1, name = "A.S. Roma", description = u"Associazione Sportiva Roma, commonly referred to as simply Roma, is a professional Italian football club based in Rome. Founded by a merger arranged by the Fascist regime in 1927, Roma have participated in the top-tier of Italian football for all of their existence except for 1951–52. For their 63rd season in a row (82nd overall), Roma are competing in Serie A for the 2014–15 season.", image_url = "http://upload.wikimedia.org/wikipedia/en/thumb/5/52/AS_Roma_logo_%282013%29.svg/278px-AS_Roma_logo_%282013%29.svg.png", category = italy))
database_session.commit()

print "added items!"
