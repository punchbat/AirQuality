<!-- ABOUT THE PROJECT -->

## AirQuality

Welcome to AirQuality, the real-time air monitoring solution designed to provide comprehensive insights into environmental conditions. Our system utilizes advanced sensors to measure key air quality parameters including CO2 levels, temperature, and humidity. Each sensor feeds data directly to our intuitive frontend interface, ensuring you have access to the latest readings at your fingertips.

**Real-Time Data Visualization**
AirQuality’s interactive dashboard displays real-time data from various sensors located in different environments. Users can view current conditions and track changes over time, enabling informed decision-making about air quality management.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#starting-the-project">Starting the Project</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

### Techologies

- **Frontend**:

  - [![Ant Design][Antd]][Antd-url]: User interface designed with Ant Design.
  - [![React.js][React.js]][React-url]: Frontend built using React.js.
  - [![Redux][Redux]][Redux-url]: State management.
  - [![Sass][Sass]][Sass-url]: Styles preprocessor.

- **Development Tools**:

  - [![Vite][Vite]][Vite-url]: Development infrastructure.
  - [![Babel][Babel]][Babel-url]: JavaScript transpiler.
  - [![npm][npm]][npm-url]: Package manager.
  - [![ESLint][ESLint]][Eslint-url]: Code linting.
  - [![Prettier][Prettier]][Prettier-url]: Code formatting.
  - [![Stylelint][Stylelint]][Stylelint-url]: Styles linting.

- **Backend**:

  - [![Python][Python]][Python-url]: Backend developed in Python.
  - [![PostgreSQL][PostgresQL]][PostgresQL-url]: Database management system.
  - [![RabbitMQ][RabbitMQ]][RabbitMQ-url]: Message broker system.
  - [![Redis][Redis]][Redis-url]: Cache management system.
  - ![JWT][JWT]: JSON Web Tokens for authentication.
  - [![Postman][Postman]][Postman-url]: API testing.
  - [![Swagger][Swagger]][Swagger-url]: API documentation.
  - [![Docker][Docker]][Docker-url]: Containerization.

- **IDE**:
  - [![Visual Studio Code][VSCode]][VSCode-url]: Development environment.

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Node.js**:

  Make sure you have Node.js installed on your system. You can download and install Node.js from the official website: [Node.js Download](https://nodejs.org/)

- **npm**:

  npm (Node Package Manager) comes bundled with Node.js. However, it's a good practice to make sure you have the latest version of npm. You can update npm using the following command:

  ```sh
  npm install -g npm@latest
  ```

- **Python**:

  You'll need Python (Python) to run the backend of the AirQuality project. You can download and install Python from the official website: [Python Downloads](https://www.python.org/)

- **Docker**:

  If you plan to use Docker for containerization, make sure Docker is installed on your system. You can download and install Docker from the official website: [Docker Download](https://www.docker.com/products/docker-desktop/)

Now you have successfully installed all the necessary prerequisites.

<p align="right">(<a href="#about">back to top</a>)</p>

### Installation

To install and run the project locally, follow these steps:

1. Clone the repo

   ```sh
   git clone git@github.com:punchbat/AirQuality.git
   ```

2. Change to the project directory

   ```sh
   cd ./AirQuality
   ```

3. Install client-side dependencies

   ```sh
   cd ./client && docker compose up
   ```

4. Install server-side dependencies

   ```sh
   cd ./server && docker compose up
   cd ./producer && docker compose up
   ```

Now you have successfully installed all the necessary dependencies.

<p align="right">(<a href="#about">back to top</a>)</p>

### Starting the Project

1. Start the client-side

   ```sh
   make start_client
   ```

   The client will be available at <http://localhost:8000>

2. Start the server-side

   ```sh
   make start_server
   ```

   The server will be running on port <http://localhost:8000>

- Frontend: <http://localhost:8080>
- Backend: <http://localhost:8000>
- PostgreSQL Database: <http://localhost:5432>
- RabbitMQ: <http://localhost:5672>
- RabbitMQ UI: <http://localhost:15672>
- Redis: <http://localhost:6379>

<p align="right">(<a href="#about">back to top</a>)</p>

<!-- USAGE -->

## Usage

Here are the instructions for using the AirQuality platform:

1. **User Registration**: If you're a new user, start by registering an account on the AirQuality platform.

2. **Logging In**: After registration, log in with your credentials to access the platform.

3. **Creating Requests**:

   - Once logged in, you can create new requests.
   - Choose whether the request should be private or public, depending on your preferences.
   - Describe your request and provide any necessary details.

4. **Managing Requests**:

   - Users can view and manage their requests from the dashboard.
   - Managers will review and process these requests.

5. **Notifications**:

   - Stay updated with the notification system.
   - Receive instant notifications when managers respond to your requests.

6. **Manager Interaction**:

   - Managers can access the platform to process and respond to user requests.
   - Ensure prompt and accurate service to users.

7. **Data Confidentiality**:

   - Rest assured that your requests and responses are secure.
   - The platform employs robust mechanisms to protect your data from unauthorized access.

8. **Enjoy the Platform**:
   - Explore the features and benefits of the AirQuality platform.

Feel free to reach out to the project contributors for any questions or assistance with using the platform.

<p align="right">(<a href="#about">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#about">back to top</a>)</p>

<!-- CONTACT -->

## Contact

<img src='images/monkey_coding.gif' align='left'>

### Hi 👋, I`m Abat from Kazakhstan

- 🌐 My [linkedin](https://www.linkedin.com/in/akassymov/), [telegram](https://t.me/gggwws)
- 💬 Ask me about anything, I am happy to help
- 🌱 If you have any suggestions, I am open to cooperation
- 🔭 Now I’m thinking about growing towards management, let’s see what comes of it :)

<p align="right">(<a href="#about">back to top</a>)</p>

[product-screenshot]: images/main.png
[Antd]: https://img.shields.io/badge/Ant%20Design-1890FF?style=for-the-badge&logo=antdesign&logoColor=white
[Antd-url]: https://ant.design/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Redux]: https://img.shields.io/badge/Redux-593D88?style=for-the-badge&logo=redux&logoColor=white
[Redux-url]: https://redux.js.org/
[Sass]: https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white
[Sass-url]: https://sass-lang.com/
[Vite]: https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E
[Vite-url]: https://vite-docs-ru.vercel.app/
[Babel]: https://img.shields.io/badge/Babel-F9DC3E?style=for-the-badge&logo=babel&logoColor=white
[Babel-url]: https://babeljs.io/
[npm]: https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white
[npm-url]: https://www.npmjs.com/
[Eslint]: https://img.shields.io/badge/eslint-3A33D1?style=for-the-badge&logo=eslint&logoColor=white
[Eslint-url]: https://eslint.org/
[Prettier]: https://img.shields.io/badge/prettier-1A2C34?style=for-the-badge&logo=prettier&logoColor=F7BA3E
[Prettier-url]: https://prettier.io/
[Stylelint]: https://img.shields.io/badge/stylelint-000?style=for-the-badge&logo=stylelint&logoColor=white
[Stylelint-url]: https://stylelint.io/
[Python]: https://img.shields.io/badge/Python-ffde57?style=for-the-badge&logo=Python&logoColor=white
[Python-url]: https://www.python.org/
[PostgresQL]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[PostgresQL-url]: https://www.postgresql.org/
[RabbitMQ]: https://img.shields.io/badge/RabbitMQ-316192?style=for-the-badge&logo=rabbitmq&logoColor=white
[RabbitMQ-url]: https://www.rabbitmq.com/
[Redis]: https://img.shields.io/badge/Redis-316192?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/
[JWT]: https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white
[Postman]: https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white
[Postman-url]: https://www.postman.com/
[Swagger]: https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white
[Swagger-url]: https://swagger.io/
[Docker]: https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[VSCode]: https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white
[VSCode-url]: https://code.visualstudio.com/
