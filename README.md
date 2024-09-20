Virtual Manager pro-Hypervisor (working title)
I'm just starting out and I've never comprehended coding, I still don't so I've been taking all coding from ChatGPT, I wanna upfront about that. So I'm seeking someone that wanna help out managing this project. 
I'm also not very knowledgeable when it comes to Linux but I'm doing my best to try and learn.

Current features:
-Glorified concept.

What are the goals?
- To be as close to an all-in-one solution as it can be.
- Basically Proxmox, but unlike Proxmox this is going to act as an OS, something lightweight you can use and manage on the host machine with the focus on virtualizing and containering everything.
- Create and manage VMs and Docker containers in a very user-friendly way.
- Create presets for new users, example: You click the preset button and get presented by a few options like "Enterprise", "Gaming" or something else, it'll then download for example Mint and start that VM for the user.
- Eliminate the need for having preloaded ISOs, USB sticks are cheap, but it's an extra cost I wanna eliminate by just needing one for VMproHV.
- Eliminate the need for searching around for said ISOs then having to use Etcher or Rufus, restart and it's just a mess, the more convenient is Ventoy, but you still need to hunt down the ISOs, I want VMproHV to do that for the user.
- Be able to as seamlessly as possible swap from for example Windows to Linux with a key combo (Another combo would just let you access VMproHV).
- Swapping would pause or shut down the current VM while resuming the other and shift focus to that VM.
- Docker containers should have a priority list to where it's either shut down, paused or active in the background depending on what VM you launch, but should be controlled on-the-fly as well in case you wanna to a change for now or change the script.
- The less terminal usage a user has to do, the better. this is to make Windows users like myself more accepting of VMproHV, to leaviate that, the buttons could run a terminal daemon in the background launching commands.
- Single GPU splitting functionality.
- Multiple GPU splitting or focusing functionality.
- One-click update to repo and look for updates for VMproHV and the same for to upgrade the repo and VMproHV

Author: 
- ExcessFrozdy or EquallyEpic Frozdy

Contributors:
- Frozdy

Thanks:
- Github
- OpenAI ChatGPT
- Python

"Special thanks":
- Anti-consumer Died Off Before Ending | After Effects CS6
