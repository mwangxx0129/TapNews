# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer

news1 = """
(CNN)President Donald Trump on Saturday again attacked a federal judge whose decision he disliked, blasting Judge James Robart, a George W. Bush appointee who temporarily stopped his controversial travel ban Friday night.

Trump's increasingly heated responses quickly drew objections from Democrats, who said he was improperly attacking an independent judiciary. By Saturday afternoon, Trump had stepped up his criticism: "Because the ban was lifted by a judge, many very bad and dangerous people may be pouring into our country. A terrible decision."
Shortly after 8 a.m. ET, the President tweeted, "The opinion of this so-called judge, which essentially takes law-enforcement away from our country, is ridiculous and will be overturned."
The opinion of this so-called judge, which essentially takes law-enforcement away from our country, is ridiculous and will be overturned!

— Donald J. Trump (@realDonaldTrump) February 4, 2017
That tweet was one of several Trump issued Saturday morning in which he defended his executive order on immigration, which bars citizens of seven Muslim-majority countries from entering the US for 90 days, all refugees for 120 days and indefinitely halts refugees from Syria.
RELATED: James Robart: 5 things to know about judge who blocked travel ban
"When a country is no longer able to say who can, and who cannot , come in & out, especially for reasons of safety &.security - big trouble," Trump next tweeted.
When a country is no longer able to say who can, and who cannot , come in & out, especially for reasons of safety &.security - big trouble!

— Donald J. Trump (@realDonaldTrump) February 4, 2017
"Interesting that certain Middle-Eastern countries agree with the ban. They know if certain people are allowed in it's death & destruction," he added, though he didn't name any countries.
Interesting that certain Middle-Eastern countries agree with the ban. They know if certain people are allowed in it's death & destruction!

— Donald J. Trump (@realDonaldTrump) February 4, 2017
Saturday afternoon, Trump resumed his criticism, tweeting: "What is our country coming to when a judge can halt a Homeland Security travel ban and anyone, even with bad intentions, can come into U.S.?"
What is our country coming to when a judge can halt a Homeland Security travel ban and anyone, even with bad intentions, can come into U.S.?

— Donald J. Trump (@realDonaldTrump) February 4, 2017
He followed up with, "Because the ban was lifted by a judge, many very bad and dangerous people may be pouring into our country. A terrible decision."
Because the ban was lifted by a judge, many very bad and dangerous people may be pouring into our country. A terrible decision

— Donald J. Trump (@realDonaldTrump) February 4, 2017
And he was still tweeting about it early Saturday evening: "Why aren't the lawyers looking at and using the Federal Court decision in Boston, which is at conflict with ridiculous lift ban decision?"
Why aren't the lawyers looking at and using the Federal Court decision in Boston, which is at conflict with ridiculous lift ban decision?

— Donald J. Trump (@realDonaldTrump) February 4, 2017
Trump was referring to a decision by a federal judge in Boston earlier Friday, a more limited ruling that declined to renew a temporary restraining order in Massachusetts. It would have prohibited the detention or removal of foreign travelers legally authorized to come to the Boston area, and the decision represented the Trump administration's first court victory regarding the order.
Unusual criticism
It is highly unusual for a President to publicly criticize a federal judge, but during the campaign, Trump memorably railed against Judge Gonzalo Curiel, who was overseeing a lawsuit against Trump University. Trump said Curiel, who was born in Indiana, was unable to fairly preside over the lawsuit because of his "Mexican heritage." Trump had introduced plans to build a wall along the Mexican border and take a hard stance on immigration.
Vice President Mike Pence later defended Trump in an interview with ABC News' George Stephanopoulos.
"Is it right for the President to say 'so-called' judge'? Doesn't that undermine the separation of powers in the Constitution?" Stephanopoulos asked Pence on "This Week" in a clip released Saturday afternoon.
"I don't think it does," Pence replied. "I think the American people are very accustomed to this president speaking his mind and speaking very straight with them."

ABC Breaking News | Latest News Videos
But Democrats pounced on Trump's criticism of Robart, with Democratic senators flatly saying the President's comments will factor into the confirmation hearings for Supreme Court nominee Neil Gorsuch.
"Attack on federal judge from POTUS is beneath the dignity of that office. That attitude can lead America to calamity," Washington Gov. Jay Inslee tweeted Saturday.
Attack on federal judge from POTUS is beneath the dignity of that office. That attitude can lead America to calamity.

— Governor Jay Inslee (@GovInslee) February 4, 2017
"The President's attack on Judge James Robart, a Bush appointee who passed with 99 votes, shows a disdain for an independent judiciary that doesn't always bend to his wishes and a continued lack of respect for the Constitution, making it more important that the Supreme Court serve as an independent check on the administration," Senate Minority Leader Chuck Schumer said in a statement.
"With each action testing the Constitution, and each personal attack on a judge, President Trump raises the bar even higher for Judge Gorsuch's nomination to serve on the Supreme Court. His ability to be an independent check will be front and center throughout the confirmation process."
Vermont. Sen. Patrick Leahy, the ranking member of the Judiciary Committee, said Trump's "hostility toward the rule of law is not just embarrassing, it is dangerous."
"We need a nominee for the Supreme Court willing to demonstrate he or she will not cower to an overreaching executive. This makes it even more important that Judge Gorsuch, and every other judge this president may nominate, demonstrates the ability to be an independent check and balance on an administration that shamefully and harmfully seems to reject the very concept."
Robart's order on Friday was a significant setback to Trump's ban and set up the nation for a second straight weekend of confusion about the policy's legality.
The White House said Friday the Department of Justice will challenge the decision. In a statement, White House press secretary Sean Spicer initially called Robart's order "outrageous" before quickly issuing another statement that dropped that word.
Robart has presided in the US District Court for the Western District of Washington state since 2004. He assumed senior status in 2016.
"""
news2 = """
President Donald Trump on Saturday again attacked a federal judge whose decision he disliked, criticizing Judge James Robart, a George W. Bush appointee who temporarily stopped his controversial travel ban Friday night.

President Trump’s attacks quickly drew objections from Democrats, who said he was attacking an independent judiciary. And by Saturday afternoon, President Trump was openly accusing Robart of potentially allowing “many very bad and dangerous people” to flow into the US and warning of dire consequences if the executive order is not enforced.

He also said, “What is our country coming to when a judge can halt a Homeland Security ban and anyone, even with bad intentions, can come into the U.S.?”

What is our country coming to when a judge can halt a Homeland Security travel ban and anyone, even with bad intentions, can come into U.S.?

— Donald J. Trump (@realDonaldTrump) February 4, 2017

Shortly after 8 a.m. ET, the President tweeted, “The opinion of this so-called judge, which essentially takes law-enforcement away from our country, is ridiculous and will be overturned.”

The opinion of this so-called judge, which essentially takes law-enforcement away from our country, is ridiculous and will be overturned!

— Donald J. Trump (@realDonaldTrump) February 4, 2017

The tweet was one of several President Trump issued Saturday morning in which he defended his executive order on immigration, which bars citizens of seven Muslim-majority countries from entering the US for 90 days, all refugees for 120 days and indefinitely halts refugees from Syria.

“When a country is no longer able to say who can, and who cannot , come in & out, especially for reasons of safety &.security – big trouble,” President Trump next tweeted.

When a country is no longer able to say who can, and who cannot , come in & out, especially for reasons of safety &.security – big trouble!

— Donald J. Trump (@realDonaldTrump) February 4, 2017

“Interesting that certain Middle-Eastern countries agree with the ban. They know if certain people are allowed in it’s death & destruction,” he added, though he didn’t name any countries.

Interesting that certain Middle-Eastern countries agree with the ban. They know if certain people are allowed in it's death & destruction!

— Donald J. Trump (@realDonaldTrump) February 4, 2017

Saturday afternoon, President Trump resumed his criticism, tweeting: “What is our country coming to when a judge can halt a Homeland Security travel ban and anyone, even with bad intentions, can come into U.S.?”

He followed up with, “Because the ban was lifted by a judge, many very bad and dangerous people may be pouring into our country. A terrible decision.”

Because the ban was lifted by a judge, many very bad and dangerous people may be pouring into our country. A terrible decision

— Donald J. Trump (@realDonaldTrump) February 4, 2017

It is highly unusual for a President to publicly criticize a federal judge, but during the campaign, President Trump memorably railed against Judge Gonzalo Curiel, who was overseeing a lawsuit against Trump University. President Trump said Curiel, who was born in Indiana, was unable to fairly preside over the lawsuit because of his “Mexican heritage.” President Trump had introduced plans to build a wall along the Mexican border and take a hard stance on immigration.

Democrats pounced on President Trump’s criticism of Robart, with Democratic senators flatly saying the President’s comments will factor into the confirmation hearings for Supreme Court nominee Neil Gorsuch.

“Attack on federal judge from POTUS is beneath the dignity of that office. That attitude can lead America to calamity,” Washington Gov. Jay Inslee tweeted Saturday.

Attack on federal judge from POTUS is beneath the dignity of that office. That attitude can lead America to calamity.

— Governor Jay Inslee (@GovInslee) February 4, 2017

“The President’s attack on Judge James Robart, a Bush appointee who passed with 99 votes, shows a disdain for an independent judiciary that doesn’t always bend to his wishes and a continued lack of respect for the Constitution, making it more important that the Supreme Court serve as an independent check on the administration,” Senate Minority Leader Chuck Schumer said in a statement.

“With each action testing the Constitution, and each personal attack on a judge, President Trump raises the bar even higher for Judge Gorsuch’s nomination to serve on the Supreme Court. His ability to be an independent check will be front and center throughout the confirmation process.”

Vermont. Sen. Patrick Leahy, the ranking member of the Judiciary Committee, said President Trump’s “hostility toward the rule of law is not just embarrassing, it is dangerous.”

“We need a nominee for the Supreme Court willing to demonstrate he or she will not cower to an overreaching executive. This makes it even more important that Judge Gorsuch, and every other judge this president may nominate, demonstrates the ability to be an independent check and balance on an administration that shamefully and harmfully seems to reject the very concept.”

Robart’s order on Friday was a significant setback to President Trump’s ban and set up the nation for a second straight weekend of confusion about the policy’s legality.

The White House said Friday the Department of Justice will challenge the decision. In a statement, White House press secretary Sean Spicer initially called Robart’s order “outrageous” before quickly issuing another statement that dropped that word.

Robart has presided in the US District Court for the Western District of Washington state since 2004. He assumed senior status in 2016.
"""

documents = [news1, news2]

tfidf = TfidfVectorizer().fit_transform(documents)
pairwise_sim = tfidf * tfidf.T

print pairwise_sim.A