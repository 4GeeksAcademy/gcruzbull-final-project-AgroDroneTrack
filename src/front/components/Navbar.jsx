import { Link } from "react-router-dom";


export const Navbar = () => {
	return (
		<nav className="navbar navbar-expand-md navbar-light bg-white border-bottom shadow-sm sticky-top">
			<div className="container">
				{/* Contenedor 1: Logo */}
				<Link to="/" className="navbar-brand d-flex align-items-center">
					<div className="bg-success p-2 rounded me-2 d-flex align-items-center justify-content-center">
						logo
					</div>
					<div className="d-flex align-items-baseline">
						<span className="fs-4 fw-bold text-dark">AgriVision</span>
						<span className="fs-5 fw-medium text-success ms-1">AI</span>
					</div>
				</Link>

				{/* Botón hamburguesa para móviles */}
				<button
					className="navbar-toggler"
					type="button"
					data-bs-toggle="collapse"
					data-bs-target="#navbarNav"
					aria-controls="navbarNav"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<span className="navbar-toggler-icon"></span>
					{/* <Menu size={24} /> */}
				</button>

				{/* Contenido colapsable */}
				<div className="collapse navbar-collapse" id="navbarNav">
					{/* Enlaces de navegación */}
					<ul className="navbar-nav ms-auto mb-2 mb-md-0 me-3">
						<li className="nav-item mx-3">
							<Link to="/" className="nav-link text-dark fw-bold">
								Inicio
							</Link>
						</li>
						<li className="nav-item mx-3">
							<Link to="/dashboard" className="nav-link text-dark fw-bold">
								Dashboard
							</Link>
						</li>
						<li className="nav-item mx-3">
							<Link to="/about" className="nav-link text-dark fw-bold">
								Nosotros
							</Link>
						</li>
						<li className="nav-item mx-3">
							<Link to="/contact" className="nav-link text-dark fw-bold">
								Contacto
							</Link>
						</li>
					</ul>

					{/* Botones de autenticación */}
					<div className="d-flex align-items-center gap-2">
						<Link to="/login" className="d-flex btn btn-outline-secondary me-3 my-3 p-1">
							<span className="d-flex px-2 py-1">
								<i className="fa-solid px-2 pt-1 fa-arrow-right-to-bracket"></i>
								<p className="text-black fw-bold mb-0 pe-2">Ingresar</p>
							</span>	
						</Link>
						{/* <Link to="/login" className="btn btn-outline-secondary d-flex align-items-center gap-1">
							<Login size={16} />
							<span>Ingresar</span>
						</Link> */}
						<Link to="/profile" className="d-flex btn btn-success ms-2 my-3 text-white align-content-center">
							{/* <User size={16} /> */}
							<span className="px-2 mb-1"><p className="fw-bold mb-0 pe-2">Perfil</p></span>
						</Link>
					</div>
				</div>
			</div>
		</nav>







		// <nav className="navbar navbar-expand-md navbar-light bg-white border-bottom shadow-sm sticky-top">
		// 	<div className="container">
		// 		{/* Contenedor 1: Logo */}
		// 		<div>
		// 			<Link to="/" className="navbar-brand d-flex align-items-center">
		// 				<div className="bg-success p-2 rounded me-2">
		// 					<i>Hoja</i>
		// 				</div>
		// 				<div>
		// 					<span className="fw-bold text-dark fs-4">AgriVision</span>
		// 					<span className="fw-medium text-success fs-5 ms-1">AI</span>
		// 				</div>
		// 			</Link>
				

		// 		{/* Mobile toggle button */}
		// 		<button
		// 			className="navbar-toggler"
		// 			type="button"
		// 			data-bs-toggle="collapse"
		// 			data-bs-target="#navbarContent"
		// 			aria-controls="navbarContent"
		// 			aria-expanded="false"
		// 			aria-label="Toggle navigation"
		// 		>
		// 			<span className="navbar-toggler-icon"></span>
		// 		</button>

		// 		</div>

		// 		{/* Contenedor 2: Nav links */}
		// 		<div className="d-flex justify-items-between align-content-center collapse navbar-collapse" id="navbarContent">
		// 			<ul className="navbar-nav m-auto mb-2 mb-md-0">
		// 				<li className="nav-item mx-5">
		// 					<Link to="/" className="nav-link text-dark">
		// 						Inicio
		// 					</Link>
		// 				</li>
		// 				<li className="nav-item mx-5">
		// 					<Link to="/dashboard" className="nav-link text-dark">
		// 						Dashboard
		// 					</Link>
		// 				</li>
		// 				<li className="nav-item mx-5">
		// 					<Link to="/about" className="nav-link text-dark">
		// 						Nosotros
		// 					</Link>
		// 				</li>
		// 				<li className="nav-item mx-5">
		// 					<Link to="/contact" className="nav-link text-dark">
		// 						Contacto
		// 					</Link>
		// 				</li>
		// 			</ul>
		// 		</div>

				

		// 		{/* Contenedor 3: Auth buttons */}
		// 		<div className="d-flex">
						// <Link to="/login" className="d-flex btn btn-outline-secondary me-5 p-2">
						// 	<i className="fa-solid pe-2 pt-1 fa-arrow-right-to-bracket"></i>
						// 	<p className="mb-0">Ingresar</p>
						// </Link>
		// 				<Link to="/profile" className="btn btn-success text-white p-2">
		// 					Perfil
		// 				</Link>
		// 		</div>
		// 	</div>
		// </nav>




		// <nav className="navbar navbar-expand-md navbar-light bg-white border-bottom shadow-sm sticky-top">
		// 	<div className="container">
		// 		<div className="row">
		// 			<div className="col-lg-3 col-md-3">
		// 				{/* Logo */}
		// 				<Link to="/" className="navbar-brand d-flex align-items-center">
		// 					<div className="bg-success p-2 rounded me-2">
		// 						{/* <Leaf className="text-white" /> */}
		// 					</div>
		// 					<div>
		// 						<span className="fw-bold text-dark fs-4">AgriVision</span>
		// 						<span className="fw-medium text-success fs-5 ms-1">AI</span>
		// 					</div>
		// 				</Link>

		// 				{/* Mobile toggle button */}
		// 				<button
		// 					className="navbar-toggler"
		// 					type="button"
		// 					data-bs-toggle="collapse"
		// 					data-bs-target="#navbarContent"
		// 					aria-controls="navbarContent"
		// 					aria-expanded="false"
		// 					aria-label="Toggle navigation"
		// 				>
		// 					<span className="navbar-toggler-icon"></span>
		// 				</button>
		// 			</div>

		// 			<div className="col-lg-6 col-md-6">
		// 				{/* Nav links */}
		// 				<div className="collapse navbar-collapse" id="navbarContent">
		// 					<ul className="navbar-nav me-auto mb-2 mb-md-0">
		// 						<li className="nav-item">
		// 							<Link to="/" className="nav-link text-dark">
		// 								Inicio
		// 							</Link>
		// 						</li>
		// 						<li className="nav-item">
		// 							<Link to="/dashboard" className="nav-link text-dark">
		// 								Dashboard
		// 							</Link>
		// 						</li>
		// 						<li className="nav-item">
		// 							<Link to="/about" className="nav-link text-dark">
		// 								Nosotros
		// 							</Link>
		// 						</li>
		// 						<li className="nav-item">
		// 							<Link to="/contact" className="nav-link text-dark">
		// 								Contacto
		// 							</Link>
		// 						</li>
		// 					</ul>
		// 				</div>
		// 			</div>

		// 			<div className="col-lg-3 col-md-3">
		// 				{/* Auth buttons */}
		// 				<div className="d-flex">
		// 					<Link to="/login" className="btn btn-outline-secondary me-2">
		// 						Ingresar
		// 					</Link>
		// 					<Link to="/profile" className="btn btn-success text-white">
		// 						Perfil
		// 					</Link>
		// 				</div>
		// 			</div>
		// 		</div>

		// 	</div>
		// </nav>
		
	);
};







// <nav className="navbar navbar-light bg-light">
// 	<div className="container">
// 		<Link to="/">
// 			<span className="navbar-brand mb-0 h1">React Boilerplate</span>
// 		</Link>
// 		<div className="ml-auto">
// 			<Link to="/demo">
// 				<button className="btn btn-primary">Check the Context in action</button>
// 			</Link>
// 		</div>
// 	</div>