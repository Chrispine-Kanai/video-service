Model Architecture planning

<p>Membership</p>
| slug | type(Free, Pro, enterprise) | price | stripe plan id |

<p>UserMembership</p>
| user {foreign key to default user} | stripe customer id | membership type {foreign key to membership} |

<p>Subscription</p>
| user membership  {foreign key to UserMembership} | stripe subscription id {foreign key to UserMembership} | active |

<p>Course</p>
| slug | title | description | allowed memberships  {foreign key to Membership} |

<p>Lesson</p>
| slug | title | stripe plan id | course {foreign key to Course} | position | video | thumbnail |
