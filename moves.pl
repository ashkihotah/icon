move(Input) :-
    sub_string(Input, Before, _, After, ' ['),
    NewAfter is After - 1,
    sub_string(Input, 0, Before, _, Move),
    sub_string(Input, _, NewAfter, 1, Type),
    type(Type),
    move(Move).

move("Absorb").
move("Accelerock").
move("Acid").
move("Acid Armor").
move("Acid Spray").
move("Acrobatics").
move("Acupressure").
move("Aerial Ace").
move("Aeroblast").
move("After You").
move("Agility").
move("Air Cutter").
move("Air Slash").
move("Ally Switch").
move("Amnesia").
move("Anchor Shot").
move("Ancient Power").
move("Apple Acid").
move("Aqua Jet").
move("Aqua Ring").
move("Aqua Tail").
move("Arm Thrust").
move("Aromatherapy").
move("Aromatic Mist").
move("Assist").
move("Assurance").
move("Astonish").
move("Astral Barrage").
move("Attack Order").
move("Attract").
move("Aura Sphere").
move("Aura Wheel").
move("Aurora Beam").
move("Aurora Veil").
move("Autotomize").
move("Avalanche").
move("Baby Doll Eyes").
move("Baddy Bad").
move("Baneful Bunker").
move("Barrage").
move("Barrier").
move("Baton Pass").
move("Beak Blast").
move("Beat Up").
move("Behemoth Bash").
move("Behemoth Blade").
move("Belch").
move("Belly Drum").
move("Bestow").
move("Bide").
move("Bind").
move("Bite").
move("Blast Burn").
move("Blaze Kick").
move("Blizzard").
move("Block").
move("Blue Flare").
move("Body Press").
move("Body Slam").
move("Bolt Beak").
move("Bolt Strike").
move("Bone Club").
move("Bone Rush").
move("Bonemerang").
move("Boomburst").
move("Bounce").
move("Bouncy Bubble").
move("Branch Poke").
move("Brave Bird").
move("Breaking Swipe").
move("Brick Break").
move("Brine").
move("Brutal Swing").
move("Bubble").
move("Bubble Beam").
move("Bug Bite").
move("Bug Buzz").
move("Bulk Up").
move("Bulldoze").
move("Bullet Punch").
move("Bullet Seed").
move("Burn Up").
move("Burning Jealousy").
move("Buzzy Buzz").
move("Calm Mind").
move("Camouflage").
move("Captivate").
move("Catastropika").
move("Celebrate").
move("Charge").
move("Charge Beam").
move("Charm").
move("Chatter").
move("Chip Away").
move("Circle Throw").
move("Clamp").
move("Clanging Scales").
move("Clangorous Soul").
move("Clangorous Soulblaze").
move("Clear Smog").
move("Close Combat").
move("Coaching").
move("Coil").
move("Comet Punch").
move("Confide").
move("Confuse Ray").
move("Confusion").
move("Constrict").
move("Conversion").
move("Conversion 2").
move("Copycat").
move("Core Enforcer").
move("Corrosive Gas").
move("Cosmic Power").
move("Cotton Guard").
move("Cotton Spore").
move("Counter").
move("Court Change").
move("Covet").
move("Crabhammer").
move("Crafty Shield").
move("Cross Chop").
move("Cross Poison").
move("Crunch").
move("Crush Claw").
move("Crush Grip").
move("Curse").
move("Cut").
move("Dark Pulse").
move("Dark Void").
move("Darkest Lariat").
move("Dazzling Gleam").
move("Decorate").
move("Defend Order").
move("Defense Curl").
move("Defog").
move("Destiny Bond").
move("Detect").
move("Diamond Storm").
move("Dig").
move("Disable").
move("Disarming Voice").
move("Discharge").
move("Dive").
move("Dizzy Punch").
move("Doom Desire").
move("Double Edge").
move("Double Hit").
move("Double Iron Bash").
move("Double Kick").
move("Double Slap").
move("Double Team").
move("Draco Meteor").
move("Dragon Ascent").
move("Dragon Breath").
move("Dragon Claw").
move("Dragon Dance").
move("Dragon Darts").
move("Dragon Energy").
move("Dragon Hammer").
move("Dragon Pulse").
move("Dragon Rage").
move("Dragon Rush").
move("Dragon Tail").
move("Drain Punch").
move("Draining Kiss").
move("Dream Eater").
move("Drill Peck").
move("Drill Run").
move("Drum Beating").
move("Dual Chop").
move("Dual Wingbeat").
move("Dynamax Cannon").
move("Dynamic Punch").
move("Earth Power").
move("Earthquake").
move("Echoed Voice").
move("Eerie Impulse").
move("Eerie Spell").
move("Egg Bomb").
move("Electric Terrain").
move("Electrify").
move("Electro Ball").
move("Electroweb").
move("Embargo").
move("Ember").
move("Encore").
move("Endeavor").
move("Endure").
move("Energy Ball").
move("Entrainment").
move("Eruption").
move("Eternabeam").
move("Expanding Force").
move("Explosion").
move("Extrasensory").
move("Extreme Evoboost").
move("Extreme Speed").
move("Facade").
move("Fairy Lock").
move("Fairy Wind").
move("Fake Out").
move("Fake Tears").
move("False Surrender").
move("False Swipe").
move("Feather Dance").
move("Feint").
move("Feint Attack").
move("Fell Stinger").
move("Fiery Dance").
move("Fiery Wrath").
move("Final Gambit").
move("Fire Blast").
move("Fire Fang").
move("Fire Lash").
move("Fire Pledge").
move("Fire Punch").
move("Fire Spin").
move("First Impression").
move("Fishious Rend").
move("Fissure").
move("Flail").
move("Flame Burst").
move("Flame Charge").
move("Flame Wheel").
move("Flamethrower").
move("Flare Blitz").
move("Flash").
move("Flash Cannon").
move("Flatter").
move("Fleur Cannon").
move("Fling").
move("Flip Turn").
move("Floaty Fall").
move("Floral Healing").
move("Flower Shield").
move("Fly").
move("Flying Press").
move("Focus Blast").
move("Focus Energy").
move("Focus Punch").
move("Follow Me").
move("Force Palm").
move("Foresight").
move("Forest'S Curse").
move("Foul Play").
move("Freeze Dry").
move("Freeze Shock").
move("Freezing Glare").
move("Freezy Frost").
move("Frenzy Plant").
move("Frost Breath").
move("Frustration").
move("Fury Attack").
move("Fury Cutter").
move("Fury Swipes").
move("Fusion Bolt").
move("Fusion Flare").
move("Future Sight").
move("Gastro Acid").
move("Gear Grind").
move("Gear Up").
move("Genesis Supernova").
move("Geomancy").
move("Giga Drain").
move("Giga Impact").
move("Glacial Lance").
move("Glaciate").
move("Glare").
move("Glitzy Glow").
move("Grass Knot").
move("Grass Pledge").
move("Grass Whistle").
move("Grassy Glide").
move("Grassy Terrain").
move("Grav Apple").
move("Gravity").
move("Growl").
move("Growth").
move("Grudge").
move("Guard Split").
move("Guard Swap").
move("Guardian Of Alola").
move("Guillotine").
move("Gunk Shot").
move("Gust").
move("Gyro Ball").
move("Hail").
move("Hammer Arm").
move("Happy Hour").
move("Harden").
move("Haze").
move("Head Charge").
move("Head Smash").
move("Headbutt").
move("Heal Bell").
move("Heal Block").
move("Heal Order").
move("Heal Pulse").
move("Healing Wish").
move("Heart Stamp").
move("Heart Swap").
move("Heat Crash").
move("Heat Wave").
move("Heavy Slam").
move("Helping Hand").
move("Hex").
move("Hidden Power").
move("High Horsepower").
move("High Jump Kick").
move("Hold Back").
move("Hold Hands").
move("Hone Claws").
move("Horn Attack").
move("Horn Drill").
move("Horn Leech").
move("Howl").
move("Hurricane").
move("Hydro Cannon").
move("Hydro Pump").
move("Hyper Beam").
move("Hyper Fang").
move("Hyper Voice").
move("Hyperspace Fury").
move("Hyperspace Hole").
move("Hypnosis").
move("Ice Ball").
move("Ice Beam").
move("Ice Burn").
move("Ice Fang").
move("Ice Hammer").
move("Ice Punch").
move("Ice Shard").
move("Icicle Crash").
move("Icicle Spear").
move("Icy Wind").
move("Imprison").
move("Incinerate").
move("Inferno").
move("Infestation").
move("Ingrain").
move("Instruct").
move("Ion Deluge").
move("Iron Defense").
move("Iron Head").
move("Iron Tail").
move("Jaw Lock").
move("Judgment").
move("Jump Kick").
move("Jungle Healing").
move("Karate Chop").
move("Kinesis").
move("King'S Shield").
move("Knock Off").
move("Land'S Wrath").
move("Laser Focus").
move("Lash Out").
move("Last Resort").
move("Lava Plume").
move("Leaf Blade").
move("Leaf Storm").
move("Leaf Tornado").
move("Leafage").
move("Leech Life").
move("Leech Seed").
move("Leer").
move("Lick").
move("Life Dew").
move("Light Of Ruin").
move("Light Screen").
move("Light That Burns The Sky").
move("Liquidation").
move("Lock On").
move("Lovely Kiss").
move("Low Kick").
move("Low Sweep").
move("Lucky Chant").
move("Lunar Dance").
move("Lunge").
move("Luster Purge").
move("Mach Punch").
move("Magic Coat").
move("Magic Powder").
move("Magic Room").
move("Magical Leaf").
move("Magma Storm").
move("Magnet Bomb").
move("Magnet Rise").
move("Magnetic Flux").
move("Magnitude").
move("Malicious Moonsault").
move("Mat Block").
move("Max Airstream").
move("Max Darkness").
move("Max Flare").
move("Max Flutterby").
move("Max Geyser").
move("Max Guard").
move("Max Hailstorm").
move("Max Knuckle").
move("Max Lightning").
move("Max Mindstorm").
move("Max Ooze").
move("Max Overgrowth").
move("Max Phantasm").
move("Max Quake").
move("Max Rockfall").
move("Max Starfall").
move("Max Steelspike").
move("Max Strike").
move("Max Wyrmwind").
move("Me First").
move("Mean Look").
move("Meditate").
move("Mega Drain").
move("Mega Kick").
move("Mega Punch").
move("Megahorn").
move("Memento").
move("Menacing Moonraze Maelstrom").
move("Metal Burst").
move("Metal Claw").
move("Metal Sound").
move("Meteor Assault").
move("Meteor Beam").
move("Meteor Mash").
move("Metronome").
move("Milk Drink").
move("Mimic").
move("Mind Blown").
move("Mind Reader").
move("Minimize").
move("Miracle Eye").
move("Mirror Coat").
move("Mirror Move").
move("Mirror Shot").
move("Mist").
move("Mist Ball").
move("Misty Explosion").
move("Misty Terrain").
move("Moonblast").
move("Moongeist Beam").
move("Moonlight").
move("Morning Sun").
move("Mud Bomb").
move("Mud Shot").
move("Mud Slap").
move("Mud Sport").
move("Muddy Water").
move("Multi Attack").
move("Mystical Fire").
move("Nasty Plot").
move("Natural Gift").
move("Nature Power").
move("Nature'S Madness").
move("Needle Arm").
move("Night Daze").
move("Night Shade").
move("Night Slash").
move("Nightmare").
move("No Retreat").
move("Noble Roar").
move("Nuzzle").
move("Oblivion Wing").
move("Obstruct").
move("Oceanic Operetta").
move("Octazooka").
move("Octolock").
move("Odor Sleuth").
move("Ominous Wind").
move("Origin Pulse").
move("Outrage").
move("Overdrive").
move("Overheat").
move("Pain Split").
move("Parabolic Charge").
move("Parting Shot").
move("Pay Day").
move("Payback").
move("Peck").
move("Perish Song").
move("Petal Blizzard").
move("Petal Dance").
move("Phantom Force").
move("Photon Geyser").
move("Pika Papow").
move("Pin Missile").
move("Plasma Fists").
move("Play Nice").
move("Play Rough").
move("Pluck").
move("Poison Fang").
move("Poison Gas").
move("Poison Jab").
move("Poison Powder").
move("Poison Sting").
move("Poison Tail").
move("Pollen Puff").
move("Poltergeist").
move("Pound").
move("Powder").
move("Powder Snow").
move("Power Gem").
move("Power Split").
move("Power Swap").
move("Power Trick").
move("Power Trip").
move("Power Up Punch").
move("Power Whip").
move("Precipice Blades").
move("Present").
move("Prismatic Laser").
move("Protect").
move("Psybeam").
move("Psych Up").
move("Psychic").
move("Psychic Fangs").
move("Psychic Terrain").
move("Psycho Boost").
move("Psycho Cut").
move("Psycho Shift").
move("Psyshock").
move("Psystrike").
move("Psywave").
move("Pulverizing Pancake").
move("Punishment").
move("Purify").
move("Pursuit").
move("Pyro Ball").
move("Quash").
move("Quick Attack").
move("Quick Guard").
move("Quiver Dance").
move("Rage").
move("Rage Powder").
move("Rain Dance").
move("Rapid Spin").
move("Razor Leaf").
move("Razor Shell").
move("Razor Wind").
move("Recover").
move("Recycle").
move("Reflect").
move("Reflect Type").
move("Refresh").
move("Relic Song").
move("Rest").
move("Retaliate").
move("Return").
move("Revelation Dance").
move("Revenge").
move("Reversal").
move("Rising Voltage").
move("Roar").
move("Roar Of Time").
move("Rock Blast").
move("Rock Climb").
move("Rock Polish").
move("Rock Slide").
move("Rock Smash").
move("Rock Throw").
move("Rock Tomb").
move("Rock Wrecker").
move("Role Play").
move("Rolling Kick").
move("Rollout").
move("Roost").
move("Rototiller").
move("Round").
move("Sacred Fire").
move("Sacred Sword").
move("Safeguard").
move("Sand Attack").
move("Sand Tomb").
move("Sandstorm").
move("Sappy Seed").
move("Scald").
move("Scale Shot").
move("Scary Face").
move("Scorching Sands").
move("Scratch").
move("Screech").
move("Searing Shot").
move("Searing Sunraze Smash").
move("Secret Power").
move("Secret Sword").
move("Seed Bomb").
move("Seed Flare").
move("Seismic Toss").
move("Self Destruct").
move("Shadow Ball").
move("Shadow Bone").
move("Shadow Claw").
move("Shadow Force").
move("Shadow Punch").
move("Shadow Sneak").
move("Sharpen").
move("Sheer Cold").
move("Shell Side Arm").
move("Shell Smash").
move("Shell Trap").
move("Shift Gear").
move("Shock Wave").
move("Shore Up").
move("Signal Beam").
move("Silver Wind").
move("Simple Beam").
move("Sing").
move("Sinister Arrow Raid").
move("Sizzly Slide").
move("Sketch").
move("Skill Swap").
move("Skitter Smack").
move("Skull Bash").
move("Sky Attack").
move("Sky Drop").
move("Sky Uppercut").
move("Slack Off").
move("Slam").
move("Slash").
move("Sleep Powder").
move("Sleep Talk").
move("Sludge").
move("Sludge Bomb").
move("Sludge Wave").
move("Smack Down").
move("Smart Strike").
move("Smelling Salts").
move("Smog").
move("Smokescreen").
move("Snap Trap").
move("Snarl").
move("Snatch").
move("Snipe Shot").
move("Snore").
move("Soak").
move("Soft Boiled").
move("Solar Beam").
move("Solar Blade").
move("Sonic Boom").
move("Soul Stealing 7 Star Strike").
move("Spacial Rend").
move("Spark").
move("Sparkling Aria").
move("Sparkly Swirl").
move("Spectral Thief").
move("Speed Swap").
move("Spider Web").
move("Spike Cannon").
move("Spikes").
move("Spiky Shield").
move("Spirit Break").
move("Spirit Shackle").
move("Spit Up").
move("Spite").
move("Splash").
move("Splintered Stormshards").
move("Splishy Splash").
move("Spore").
move("Spotlight").
move("Stealth Rock").
move("Steam Eruption").
move("Steamroller").
move("Steel Beam").
move("Steel Roller").
move("Steel Wing").
move("Sticky Web").
move("Stockpile").
move("Stoked Sparksurfer").
move("Stomp").
move("Stomping Tantrum").
move("Stone Edge").
move("Stored Power").
move("Storm Throw").
move("Strange Steam").
move("Strength").
move("Strength Sap").
move("String Shot").
move("Struggle").
move("Struggle Bug").
move("Stuff Cheeks").
move("Stun Spore").
move("Submission").
move("Substitute").
move("Sucker Punch").
move("Sunny Day").
move("Sunsteel Strike").
move("Super Fang").
move("Superpower").
move("Supersonic").
move("Surf").
move("Surging Strikes").
move("Swagger").
move("Swallow").
move("Sweet Kiss").
move("Sweet Scent").
move("Swift").
move("Switcheroo").
move("Swords Dance").
move("Synchronoise").
move("Synthesis").
move("Tackle").
move("Tail Glow").
move("Tail Slap").
move("Tail Whip").
move("Tailwind").
move("Take Down").
move("Tar Shot").
move("Taunt").
move("Tearful Look").
move("Teatime").
move("Techno Blast").
move("Teeter Dance").
move("Telekinesis").
move("Teleport").
move("Terrain Pulse").
move("Thief").
move("Thousand Arrows").
move("Thousand Waves").
move("Thrash").
move("Throat Chop").
move("Thunder").
move("Thunder Cage").
move("Thunder Fang").
move("Thunder Punch").
move("Thunder Shock").
move("Thunder Wave").
move("Thunderbolt").
move("Thunderous Kick").
move("Tickle").
move("Topsy Turvy").
move("Torment").
move("Toxic").
move("Toxic Spikes").
move("Toxic Thread").
move("Transform").
move("Tri Attack").
move("Trick").
move("Trick Or Treat").
move("Trick Room").
move("Triple Axel").
move("Triple Kick").
move("Trop Kick").
move("Trump Card").
move("Twineedle").
move("Twister").
move("U Turn").
move("Uproar").
move("V Create").
move("Vacuum Wave").
move("Veevee Volley").
move("Venom Drench").
move("Venoshock").
move("Vine Whip").
move("Vise Grip").
move("Vital Throw").
move("Volt Switch").
move("Volt Tackle").
move("Wake Up Slap").
move("Water Gun").
move("Water Pledge").
move("Water Pulse").
move("Water Shuriken").
move("Water Sport").
move("Water Spout").
move("Waterfall").
move("Weather Ball").
move("Whirlpool").
move("Whirlwind").
move("Wicked Blow").
move("Wide Guard").
move("Wild Charge").
move("Will O Wisp").
move("Wing Attack").
move("Wish").
move("Withdraw").
move("Wonder Room").
move("Wood Hammer").
move("Work Up").
move("Worry Seed").
move("Wrap").
move("Wring Out").
move("X Scissor").
move("Yawn").
move("Zap Cannon").
move("Zen Headbutt").
move("Zing Zap").
move("Zippy Zap").
move("G-Max Vine Lash").
move("G-Max Wildfire").
move("G-Max Cannonade").
move("G-Max Befuddle").
move("G-Max Volt Crash").
move("G-Max Gold Rush").
move("G-Max Chi Strike").
move("G-Max Terror").
move("G-Max Foam Burst").
move("G-Max Resonance").
move("G-Max Cuddle").
move("G-Max Replenish").
move("G-Max Malodor").
move("G-Max Meltdown").
move("G-Max Drum Solo").
move("G-Max Fireball").
move("G-Max Hydrosnipe").
move("G-Max Wind Rage").
move("G-Max Gravitas").
move("G-Max Stonesurge").
move("G-Max Volcalith").
move("G-Max Tartness").
move("G-Max Sweetness").
move("G-Max Sandblast").
move("G-Max Stun Shock").
move("G-Max Centiferno").
move("G-Max Smite").
move("G-Max Snooze").
move("G-Max Finale").
move("G-Max Steelsurge").
move("G-Max Depletion").
move("G-Max One Blow").
move("G-Max Rapid Flow").
