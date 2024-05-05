<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/HyScript7/fvWeb">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">fvWeb</h3>

  <p align="center">
    The official website for Fusionverse
    <br />
    <a href="https://tree.taiga.io/project/hyscript7-fvweb/wiki/home"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Demo</a>
    ·
    <a href="https://github.com/HyScript7/fvWeb/issues">Report Bug</a>
    ·
    <a href="https://github.com/HyScript7/fvWeb/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

fvWeb is the official website for [Fusionverse](https://discord.gg/Nj4ScwhnXD), written with SolidJS and FastAPI.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)
- ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
- ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
- ![PNPM](https://img.shields.io/badge/pnpm-%234a4a4a.svg?style=for-the-badge&logo=pnpm&logoColor=f69220)
- ![SolidJS](https://img.shields.io/badge/SolidJS-2c4f7c?style=for-the-badge&logo=solid&logoColor=c8c9cb)
- ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
- ![DaisyUI](https://img.shields.io/badge/daisyui-5A0EF8?style=for-the-badge&logo=daisyui&logoColor=white)
- ![NGINX](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
- ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
- Memcached

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local (development) copy up and running follow the following steps.

For production deployments, see docker-compose.yml.

### Prerequisites

- [node.js](https://nodejs.org/en)
- [npm](https://www.npmjs.com/) or [pnpm](https://pnpm.io/)
- [python](https://python.org)
- [poetry](https://python-poetry.org/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/HyScript7/fvWeb.git
   ```
2. Setup backend environment
   ```sh
   cd backend
   poetry env use python
   poetry install
   cd ..
   ```
3. Setup frontend environment
   ```sh
   cd frontend
   pnpm install
   cd ..
   ```

To run the backend:
   ```sh
   cd backend
   poetry run python3 -m app
   ```

To run tests for the backend:
   ```sh
   cd backend
   poetry run pytest --cov
   # then to generate coverage report
   poetry run coverage html
   ```

To run the frontend:
   ```sh
   cd frontend
   pnpm run dev
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

The project is currently not ready for production. This section will be expanded with screenshots and examples in the future.

_For more examples, please refer to the [Documentation](https://tree.taiga.io/project/hyscript7-fvweb/wiki/home)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [ ] Authentication
  - [ ] Authorization
- [ ] User Profiles
- [ ] Wiki
- [ ] Forum
- [ ] Blog
- [ ] Custom Pages
- [ ] Searching
- [ ] Admin

See the [open issues](https://github.com/HyScript7/fvWeb/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

HyScript7 - [@hyscript7](https://twitter.com/hyscript7) - hyscript7@gmail.com

Project Link: [https://github.com/HyScript7/fvWeb](https://github.com/HyScript7/fvWeb)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [README Template](https://github.com/othneildrew/Best-README-Template/)
- [Markdown Badges](https://ileriayo.github.io/markdown-badges/)
- [IDE Gitignore](https://salesforce.stackexchange.com/questions/321725/gitignore-for-various-ides)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/HyScript7/fvWeb.svg?style=for-the-badge
[contributors-url]: https://github.com/HyScript7/fvWeb/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HyScript7/fvWeb.svg?style=for-the-badge
[forks-url]: https://github.com/HyScript7/fvWeb/network/members
[stars-shield]: https://img.shields.io/github/stars/HyScript7/fvWeb.svg?style=for-the-badge
[stars-url]: https://github.com/HyScript7/fvWeb/stargazers
[issues-shield]: https://img.shields.io/github/issues/HyScript7/fvWeb.svg?style=for-the-badge
[issues-url]: https://github.com/HyScript7/fvWeb/issues
[license-shield]: https://img.shields.io/github/license/HyScript7/fvWeb.svg?style=for-the-badge
[license-url]: https://github.com/HyScript7/fvWeb/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
