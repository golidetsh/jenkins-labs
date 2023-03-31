function ListGroup() {

    let posts = ["Top 10 Recipes", "EPL Diaries", "Tokyo Drift Story", "Johannesburg By Night"]; 

  return (
    <>
      <h1>MyList</h1>
      <ul className="list-group">
        {posts.map((post) => (
          <li className="list-group-item" key={post}>
            {post}
          </li>
        ))}
      </ul>
    </>
  );

}

export default ListGroup;