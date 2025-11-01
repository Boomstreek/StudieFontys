```mermaid
flowchart TD
    start([start]) --> id1{loadDatabase}
    id1 -->|Database found| usernameLogin[/Wat is je username/]
    id1 -->|Database not found| createDB[createDatabase]
    createDB --> usernameLogin
    usernameLogin --> dateRecord
    dateRecord --> sbd[/"Which excersize do you want to do? (s)quat, (b)ench, (d)eadlift"/]
    
    sbd --> id2{Set Oefening as}
    id2 -->|s| set
    id2 -->|b| set
    id2 -->|d| set
    id2 --> else
    else --> sbd
    
    set --> 
    
```

Nu ik hiermee bezig ben, denk ik dat ik wel eerst een state diagram moet maken. Dit wordt anders echt spagehetti code deze flow chart.