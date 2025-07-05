import { Link } from "react-router-dom";

export const Navbar = () => {
	return (

		<nav className="navbar navbar-expand-md navbar-light bg-white border-bottom shadow-sm sticky-top">
			<div className="container">
				{/* Logo */}
				<Link to="/" className="navbar-brand d-flex align-items-center">
					<div className="bg-success p-2 rounded me-2">
						{/* <Leaf className="text-white" /> */}
					</div>
					<div>
						<span className="fw-bold text-dark fs-4">AgriVision</span>
						<span className="fw-medium text-success fs-5 ms-1">AI</span>
					</div>
				</Link>

				{/* Mobile toggle button */}
				<button
					className="navbar-toggler"
					type="button"
					data-bs-toggle="collapse"
					data-bs-target="#navbarContent"
					aria-controls="navbarContent"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<span className="navbar-toggler-icon"></span>
				</button>

				{/* Nav links */}
				<div className="collapse navbar-collapse" id="navbarContent">
					<ul className="navbar-nav me-auto mb-2 mb-md-0">
						<li className="nav-item">
							<Link to="/" className="nav-link text-dark">
								Inicio
							</Link>
						</li>
						<li className="nav-item">
							<Link to="/dashboard" className="nav-link text-dark">
								Dashboard
							</Link>
						</li>
						<li className="nav-item">
							<Link to="/about" className="nav-link text-dark">
								Nosotros
							</Link>
						</li>
						<li className="nav-item">
							<Link to="/contact" className="nav-link text-dark">
								Contacto
							</Link>
						</li>
					</ul>

					{/* Auth buttons */}
					<div className="d-flex">
						<Link to="/login" className="btn btn-outline-secondary me-2">
							Ingresar
						</Link>
						<Link to="/profile" className="btn btn-success text-white">
							Perfil
						</Link>
					</div>
				</div>
			</div>
		</nav>




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