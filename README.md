Abstract:

Due to the growth of internet usage by individuals, the security of personal information has become a prime concern, so that unauthorized person does not get access to the confidential information. Secret Sharing is the method for increasing security of data by distributing the secret among a group of participants and only when a desired number of participants come together then the secret can be recovered and hence user authentication can be achieved.

Methodology:

Registration:
On registration, server asks the following things:
Number of clients/participants
Threshold number of clients/participants

Generation of partial keys:
After registration, the server sends partial keys to all the participating client
Partial key generation is done using Shamir Secret Key Sharing Scheme

Reconstruction of secret:
On request to access secret folder from clients, atleast threshold number of participants          must share their partial keys with server.
On receiving correct shares from threshold number of participants the server(S) gives    access to secret folder.

Input and output details:

1] Input:

Enter Secret: hi

Enter Max Number of Clients: 2

Enter Threshold size:2

Output:
The Recovered secret is hi

You have access to the folder

Client1 & Client2:

![image](https://github.com/roshnishetty271/User-Authentication-using-Secret-key-Sharing/assets/144407427/2774c514-c67f-49c2-86a1-7b63ed1f9f56)



















Dealer:

![image](https://github.com/roshnishetty271/User-Authentication-using-Secret-key-Sharing/assets/144407427/55c5a512-dc41-4735-8d79-8152f5ec067e)

















  Access to the  Locker folder:


![image](https://github.com/roshnishetty271/User-Authentication-using-Secret-key-Sharing/assets/144407427/3268f4b9-9bfb-495d-a0e3-dabaf704d287)





2] Input:

Enter Secret: authentication

Enter Max Number of Clients: 2

Enter Threshold size:2

Output:

The Recovered secret is authentication

You have access to the folder

Client1 & Client2:




![image](https://github.com/roshnishetty271/User-Authentication-using-Secret-key-Sharing/assets/144407427/35bc98d8-3abc-45a1-a0f6-68c1fb501dd6)
















Dealer:


![image](https://github.com/roshnishetty271/User-Authentication-using-Secret-key-Sharing/assets/144407427/6a3e478e-393f-4a5e-a755-32d9bb02ca38)
















Access to the  Locker folder:



![image](https://github.com/roshnishetty271/User-Authentication-using-Secret-key-Sharing/assets/144407427/9204858a-44bc-47db-81da-577d2a755646)





●	Results and Discussions

If wrong shares are entered then the secret wont be reconstructed

Eg: Input:

Enter Secret: hello

Enter Max Number of Clients: 2

Enter Threshold size:2

Output:

Oops!! You have entered wrong shares

Wrong password! Please enter right password

Client1 & Client2:


![image](https://github.com/roshnishetty271/User-Authentication-using-Secret-key-Sharing/assets/144407427/5853945b-4d63-4494-933b-983d0588e3a5)













Dealer:

![image](https://github.com/roshnishetty271/User-Authentication-using-Secret-key-Sharing/assets/144407427/df2ffbeb-6549-4ecf-a482-6b8fbcec9048)
















No access to the  Locker folder:

![image](https://github.com/roshnishetty271/User-Authentication-using-Secret-key-Sharing/assets/144407427/6031ece8-6c0b-4c56-91b9-720fefa85f69)







Conclusion and Future Scope:

Security is a very serious and an important issue in any application. And to provide the security, authentication is something plays a very important role. Authentication is mainly provided through various secret sharing schemes. Secret-sharing schemes are actually very important tools in cryptography and they are used as a building box in many secure protocols, e.g., general protocol for multiparty computation, threshold cryptography, access control, attribute-based encryption, and generalized oblivious transfer. We have proposed a novel user authentication protocol which is based on two-party or more computation. This protocol is also designed to mitigate the key exposure attack when one of the user’s device is obtained or compromised by outsiders or some attackers.
Our security and performance evaluations demonstrated the practicality of our proposed protocol. However, we will need to develop a prototype implementation of the protocol in a real-world environment in order to be fully assured of its real-world utility. Therefore, one future research agenda is to collaborate with a mobile device developer to implement the proposed protocol for real-world evaluation.



